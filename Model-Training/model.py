<<<<<<< HEAD
import os
import re
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Concatenate, Input
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model

# Set data folder path
data_folder = "aqi_data"
sequence_length = 5  # Using 5 past years to predict the next year's AQI

# Create output directories
model_dir = "models"
scaler_dir = "scalers"
os.makedirs(model_dir, exist_ok=True)
os.makedirs(scaler_dir, exist_ok=True)

def train_city_model(city_name, df):
    """Train and save an LSTM model for a specific city with year as an input feature."""
    print(f" Training model for {city_name}...")

    # Normalize AQI values
    scaler = MinMaxScaler()
    df["Scaled AQI"] = scaler.fit_transform(df[["AQI Value"]])
    joblib.dump(scaler, f"{scaler_dir}/{city_name}_scaler.pkl")

    # Prepare sequences for LSTM
    X_seq, X_year, y = [], [], []

    for i in range(len(df) - sequence_length):
        X_seq.append(df["Scaled AQI"].values[i:i + sequence_length])
        X_year.append(df.index[i + sequence_length].year)  # Include the target year as input
        y.append(df["Scaled AQI"].values[i + sequence_length])

    X_seq, X_year, y = np.array(X_seq), np.array(X_year), np.array(y)

    if len(X_seq) < 5:
        print(f" Not enough data for {city_name}. Skipping...")
        return

    # Normalize the year feature
    year_scaler = MinMaxScaler()
    X_year = year_scaler.fit_transform(X_year.reshape(-1, 1))
    joblib.dump(year_scaler, f"{scaler_dir}/{city_name}_year_scaler.pkl")

    # Train-test split
    train_size = int(len(X_seq) * 0.8)
    X_train_seq, X_test_seq = X_seq[:train_size], X_seq[train_size:]
    X_train_year, X_test_year = X_year[:train_size], X_year[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Define LSTM model with two inputs
    seq_input = Input(shape=(sequence_length, 1), name="seq_input")
    year_input = Input(shape=(1,), name="year_input")

    x = LSTM(64, activation="relu", return_sequences=True)(seq_input)
    x = LSTM(64, activation="relu")(x)

    # Concatenate sequence and year input
    x = Concatenate()([x, year_input])
    x = Dense(64, activation="relu")(x)
    output = Dense(1)(x)

    model = Model(inputs=[seq_input, year_input], outputs=output)
    model.compile(optimizer="adam", loss="mse")

    # Train Model
    model.fit([X_train_seq, X_train_year], y_train, epochs=20, batch_size=16, verbose=1)

    # Save Model
    model.save(f"{model_dir}/{city_name}_model.h5")
    print(f" Model for {city_name} saved!")

# Load and process each city's data
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        city_name = re.sub(r"_AQIBulletins\.csv$", "", filename)
        city_file = os.path.join(data_folder, filename)

        df = pd.read_csv(city_file)
        df.rename(columns={"date": "Date", "Index Value": "AQI Value"}, inplace=True)
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df = df[["AQI Value"]].dropna()

        train_city_model(city_name, df)

print(" All city models trained and saved!")
=======
import os
import re
import numpy as np
import pandas as pd
import tensorflow as tf
import joblib
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Concatenate, Input
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Model

# Set data folder path
data_folder = "aqi_data"
sequence_length = 5  # Using 5 past years to predict the next year's AQI

# Create output directories
model_dir = "models"
scaler_dir = "scalers"
os.makedirs(model_dir, exist_ok=True)
os.makedirs(scaler_dir, exist_ok=True)

def train_city_model(city_name, df):
    """Train and save an LSTM model for a specific city with year as an input feature."""
    print(f" Training model for {city_name}...")

    # Normalize AQI values
    scaler = MinMaxScaler()
    df["Scaled AQI"] = scaler.fit_transform(df[["AQI Value"]])
    joblib.dump(scaler, f"{scaler_dir}/{city_name}_scaler.pkl")

    # Prepare sequences for LSTM
    X_seq, X_year, y = [], [], []

    for i in range(len(df) - sequence_length):
        X_seq.append(df["Scaled AQI"].values[i:i + sequence_length])
        X_year.append(df.index[i + sequence_length].year)  # Include the target year as input
        y.append(df["Scaled AQI"].values[i + sequence_length])

    X_seq, X_year, y = np.array(X_seq), np.array(X_year), np.array(y)

    if len(X_seq) < 5:
        print(f" Not enough data for {city_name}. Skipping...")
        return

    # Normalize the year feature
    year_scaler = MinMaxScaler()
    X_year = year_scaler.fit_transform(X_year.reshape(-1, 1))
    joblib.dump(year_scaler, f"{scaler_dir}/{city_name}_year_scaler.pkl")

    # Train-test split
    train_size = int(len(X_seq) * 0.8)
    X_train_seq, X_test_seq = X_seq[:train_size], X_seq[train_size:]
    X_train_year, X_test_year = X_year[:train_size], X_year[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Define LSTM model with two inputs
    seq_input = Input(shape=(sequence_length, 1), name="seq_input")
    year_input = Input(shape=(1,), name="year_input")

    x = LSTM(64, activation="relu", return_sequences=True)(seq_input)
    x = LSTM(64, activation="relu")(x)

    # Concatenate sequence and year input
    x = Concatenate()([x, year_input])
    x = Dense(64, activation="relu")(x)
    output = Dense(1)(x)

    model = Model(inputs=[seq_input, year_input], outputs=output)
    model.compile(optimizer="adam", loss="mse")

    # Train Model
    model.fit([X_train_seq, X_train_year], y_train, epochs=20, batch_size=16, verbose=1)

    # Save Model
    model.save(f"{model_dir}/{city_name}_model.h5")
    print(f" Model for {city_name} saved!")

# Load and process each city's data
for filename in os.listdir(data_folder):
    if filename.endswith(".csv"):
        city_name = re.sub(r"_AQIBulletins\.csv$", "", filename)
        city_file = os.path.join(data_folder, filename)

        df = pd.read_csv(city_file)
        df.rename(columns={"date": "Date", "Index Value": "AQI Value"}, inplace=True)
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)
        df = df[["AQI Value"]].dropna()

        train_city_model(city_name, df)

print(" All city models trained and saved!")
>>>>>>> ea27301 (git add)
