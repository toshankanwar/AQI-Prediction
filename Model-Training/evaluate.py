import os
import re
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Concatenate, Input
from tensorflow.keras.models import Model
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from math import sqrt

# Set paths
data_folder = "aqi_data"
model_dir = "models"
scaler_dir = "scalers"
sequence_length = 5  # Use past 5 years to predict next

# Create necessary directories
os.makedirs(model_dir, exist_ok=True)
os.makedirs(scaler_dir, exist_ok=True)

def train_city_model(city_name, df):
    print(f" Training model for {city_name}...")

    # Normalize AQI values
    scaler = MinMaxScaler()
    df["Scaled AQI"] = scaler.fit_transform(df[["AQI Value"]])
    joblib.dump(scaler, f"{scaler_dir}/{city_name}_scaler.pkl")

    X_seq, X_year, y = [], [], []
    for i in range(len(df) - sequence_length):
        X_seq.append(df["Scaled AQI"].values[i:i + sequence_length])
        X_year.append(df.index[i + sequence_length].year)
        y.append(df["Scaled AQI"].values[i + sequence_length])

    X_seq, X_year, y = np.array(X_seq), np.array(X_year), np.array(y)

    if len(X_seq) < 5:
        print(f" Not enough data for {city_name}. Skipping...")
        return

    year_scaler = MinMaxScaler()
    X_year = year_scaler.fit_transform(X_year.reshape(-1, 1))
    joblib.dump(year_scaler, f"{scaler_dir}/{city_name}_year_scaler.pkl")

    # Train-test split
    train_size = int(len(X_seq) * 0.8)
    X_train_seq, X_test_seq = X_seq[:train_size], X_seq[train_size:]
    X_train_year, X_test_year = X_year[:train_size], X_year[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Model definition
    seq_input = Input(shape=(sequence_length, 1), name="seq_input")
    year_input = Input(shape=(1,), name="year_input")
    x = LSTM(64, activation="relu", return_sequences=True)(seq_input)
    x = LSTM(64, activation="relu")(x)
    x = Concatenate()([x, year_input])
    x = Dense(64, activation="relu")(x)
    output = Dense(1)(x)

    model = Model(inputs=[seq_input, year_input], outputs=output)
    model.compile(optimizer="adam", loss="mse")
    model.fit([X_train_seq, X_train_year], y_train, epochs=20, batch_size=16, verbose=1)
    model.save(f"{model_dir}/{city_name}_model.h5")
    print(f" Model for {city_name} saved!")

def evaluate_city_model(city_name, df):
    print(f"\nEvaluating model for {city_name}...")

    # Load scalers
    scaler = joblib.load(f"{scaler_dir}/{city_name}_scaler.pkl")
    year_scaler = joblib.load(f"{scaler_dir}/{city_name}_year_scaler.pkl")

    # Create sequences
    X_seq, X_year, y = [], [], []
    for i in range(len(df) - sequence_length):
        X_seq.append(df["Scaled AQI"].values[i:i + sequence_length])
        X_year.append(df.index[i + sequence_length].year)
        y.append(df["Scaled AQI"].values[i + sequence_length])

    X_seq, X_year, y = np.array(X_seq), np.array(X_year), np.array(y)

    if len(X_seq) < 5:
        print(f" Not enough data for {city_name}. Skipping evaluation...")
        return

    X_year = year_scaler.transform(X_year.reshape(-1, 1))
    train_size = int(len(X_seq) * 0.8)
    X_test_seq, X_test_year = X_seq[train_size:], X_year[train_size:]
    y_test = y[train_size:]

    model = tf.keras.models.load_model(f"{model_dir}/{city_name}_model.h5")
    y_pred_scaled = model.predict([X_test_seq, X_test_year]).flatten()

    y_test_orig = scaler.inverse_transform(y_test.reshape(-1, 1)).flatten()
    y_pred_orig = scaler.inverse_transform(y_pred_scaled.reshape(-1, 1)).flatten()

    # Metrics
    mse = mean_squared_error(y_test_orig, y_pred_orig)
    rmse = sqrt(mse)
    mae = mean_absolute_error(y_test_orig, y_pred_orig)
    r2 = r2_score(y_test_orig, y_pred_orig)

    print(f" MSE : {mse:.2f}")
    print(f" RMSE: {rmse:.2f}")
    print(f" MAE : {mae:.2f}")
    print(f" R²  : {r2:.2f}")

    # Visualization
    years = df.index[sequence_length + train_size:]
    if len(years) != len(y_pred_orig):  # safeguard
        years = range(len(y_pred_orig))

    plt.figure(figsize=(14, 6))

    # Plot 1: Predicted vs Actual
    plt.subplot(1, 3, 1)
    plt.scatter(y_test_orig, y_pred_orig, color='dodgerblue', edgecolor='black')
    plt.xlabel("Actual AQI")
    plt.ylabel("Predicted AQI")
    plt.title(f"{city_name} - Predicted vs Actual")
    plt.plot([min(y_test_orig), max(y_test_orig)], [min(y_test_orig), max(y_test_orig)], 'r--')

    # Plot 2: Residuals
    plt.subplot(1, 3, 2)
    residuals = y_test_orig - y_pred_orig
    plt.hist(residuals, bins=20, color='orange', edgecolor='black')
    plt.title(f"{city_name} - Residuals")
    plt.xlabel("Prediction Error")

    # Plot 3: Time series
    plt.subplot(1, 3, 3)
    plt.plot(years, y_test_orig, label="Actual", marker='o')
    plt.plot(years, y_pred_orig, label="Predicted", marker='x')
    plt.title(f"{city_name} - AQI Over Time")
    plt.xlabel("Time")
    plt.ylabel("AQI")
    plt.legend()

    plt.tight_layout()
    plt.show()

# === Main pipeline ===
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        city_name = re.sub(r"_AQIBulletins\.csv$", "", filename)
        city_file = os.path.join(data_folder, filename)

        df = pd.read_csv(city_file)
        df.rename(columns={"date": "Date", "Index Value": "AQI Value"}, inplace=True)
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df = df[["AQI Value"]].dropna()

        # Train
        train_city_model(city_name, df)

        # Add Scaled AQI column again for evaluation
        df["Scaled AQI"] = MinMaxScaler().fit_transform(df[["AQI Value"]])

        # Evaluate
        evaluate_city_model(city_name, df)

print("\n✅ All city models trained, evaluated, and visualized!")
