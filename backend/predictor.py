<<<<<<< HEAD
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import os
from datetime import datetime

app = Flask(__name__)

# Directory configurations
model_dir = "models"
scaler_dir = "scalers"
sequence_length = 5
folder_path = "aqi_data/"

def find_city_file(city):
    """Find AQI CSV file for the given city."""
    file_path = os.path.join(folder_path, f"{city}_AQIBulletins.csv")
    if os.path.exists(file_path):
        return file_path
    else:
        raise FileNotFoundError(f"No AQI file found for city '{city}'.")

def load_city_data(city):
    """Load and preprocess AQI data."""
    df = pd.read_csv(find_city_file(city))
    df.rename(columns={"date": "Date", "Index Value": "AQI Value"}, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    return df.sort_index()

def find_closest_date(df, target_date):
    """Find the closest available date in the dataset matching month and day."""
    if target_date in df.index:
        return target_date
    available_dates = df.index[df.index.month == target_date.month]
    same_day = available_dates[available_dates.day == target_date.day]
    return same_day[-1] if len(same_day) > 0 else None

def prepare_input(df, date_str, scaler, year_scaler):
    """Prepare scaled input data for the LSTM model."""
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    past_values = []

    for i in range(1, sequence_length + 1):
        past_year = target_date.year - i
        past_date = target_date.replace(year=past_year)
        closest = find_closest_date(df, past_date)

        if closest:
            past_values.append(df.loc[closest, "AQI Value"])
        else:
            # Estimate missing year from prior 3 years if available
            prev_years = [past_year - j for j in range(1, 4) if past_year - j >= df.index.year.min()]
            estimate_values = []
            for y in prev_years:
                try_date = past_date.replace(year=y)
                closest = find_closest_date(df, try_date)
                if closest:
                    estimate_values.append(df.loc[closest, "AQI Value"])
            if estimate_values:
                estimate = np.mean(estimate_values)
                print(f"⚠ Estimating AQI for {past_date.date()} using 3-year average: {estimate:.2f}")
                past_values.append(estimate)
            else:
                print(f"⚠ No estimate available. Using last known AQI.")
                past_values.append(df["AQI Value"].iloc[-1])

    # Normalize AQI input using scaler (as DataFrame to avoid warnings)
    past_df = pd.DataFrame(past_values, columns=["AQI Value"])
    past_scaled = scaler.transform(past_df).reshape(1, sequence_length, 1)

    # Normalize target year using year scaler
    year_df = pd.DataFrame([[target_date.year]], columns=["year"])
    year_scaled = year_scaler.transform(year_df).reshape(1, 1)

    return [past_scaled, year_scaled]

def predict_aqi(city, date_str):
    """Predict AQI for the given city and date."""
    model_path = os.path.join(model_dir, f"{city}_model.h5")
    scaler_path = os.path.join(scaler_dir, f"{city}_scaler.pkl")
    year_scaler_path = os.path.join(scaler_dir, f"{city}_year_scaler.pkl")

    # Check model/scaler existence
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model for {city} not found.")
    if not os.path.exists(scaler_path) or not os.path.exists(year_scaler_path):
        raise FileNotFoundError(f"Scalers for {city} not found.")

    # Load model and scalers
    model = tf.keras.models.load_model(model_path)
    scaler = joblib.load(scaler_path)
    year_scaler = joblib.load(year_scaler_path)

    # Prepare data
    df = load_city_data(city)
    X_input = prepare_input(df, date_str, scaler, year_scaler)

    # Predict and inverse scale
    prediction_scaled = model.predict(X_input)
    prediction = scaler.inverse_transform(prediction_scaled)[0][0]

    return round(prediction, 2)
=======
from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import os
from datetime import datetime

app = Flask(__name__)

# Directory configurations
model_dir = "models"
scaler_dir = "scalers"
sequence_length = 5
folder_path = "aqi_data/"

def find_city_file(city):
    """Find AQI CSV file for the given city."""
    file_path = os.path.join(folder_path, f"{city}_AQIBulletins.csv")
    if os.path.exists(file_path):
        return file_path
    else:
        raise FileNotFoundError(f"No AQI file found for city '{city}'.")

def load_city_data(city):
    """Load and preprocess AQI data."""
    df = pd.read_csv(find_city_file(city))
    df.rename(columns={"date": "Date", "Index Value": "AQI Value"}, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    return df.sort_index()

def find_closest_date(df, target_date):
    """Find the closest available date in the dataset matching month and day."""
    if target_date in df.index:
        return target_date
    available_dates = df.index[df.index.month == target_date.month]
    same_day = available_dates[available_dates.day == target_date.day]
    return same_day[-1] if len(same_day) > 0 else None

def prepare_input(df, date_str, scaler, year_scaler):
    """Prepare scaled input data for the LSTM model."""
    target_date = datetime.strptime(date_str, "%Y-%m-%d")
    past_values = []

    for i in range(1, sequence_length + 1):
        past_year = target_date.year - i
        past_date = target_date.replace(year=past_year)
        closest = find_closest_date(df, past_date)

        if closest:
            past_values.append(df.loc[closest, "AQI Value"])
        else:
            # Estimate missing year from prior 3 years if available
            prev_years = [past_year - j for j in range(1, 4) if past_year - j >= df.index.year.min()]
            estimate_values = []
            for y in prev_years:
                try_date = past_date.replace(year=y)
                closest = find_closest_date(df, try_date)
                if closest:
                    estimate_values.append(df.loc[closest, "AQI Value"])
            if estimate_values:
                estimate = np.mean(estimate_values)
                print(f"⚠ Estimating AQI for {past_date.date()} using 3-year average: {estimate:.2f}")
                past_values.append(estimate)
            else:
                print(f"⚠ No estimate available. Using last known AQI.")
                past_values.append(df["AQI Value"].iloc[-1])

    # Normalize AQI input using scaler (as DataFrame to avoid warnings)
    past_df = pd.DataFrame(past_values, columns=["AQI Value"])
    past_scaled = scaler.transform(past_df).reshape(1, sequence_length, 1)

    # Normalize target year using year scaler
    year_df = pd.DataFrame([[target_date.year]], columns=["year"])
    year_scaled = year_scaler.transform(year_df).reshape(1, 1)

    return [past_scaled, year_scaled]

def predict_aqi(city, date_str):
    """Predict AQI for the given city and date."""
    model_path = os.path.join(model_dir, f"{city}_model.h5")
    scaler_path = os.path.join(scaler_dir, f"{city}_scaler.pkl")
    year_scaler_path = os.path.join(scaler_dir, f"{city}_year_scaler.pkl")

    # Check model/scaler existence
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model for {city} not found.")
    if not os.path.exists(scaler_path) or not os.path.exists(year_scaler_path):
        raise FileNotFoundError(f"Scalers for {city} not found.")

    # Load model and scalers
    model = tf.keras.models.load_model(model_path)
    scaler = joblib.load(scaler_path)
    year_scaler = joblib.load(year_scaler_path)

    # Prepare data
    df = load_city_data(city)
    X_input = prepare_input(df, date_str, scaler, year_scaler)

    # Predict and inverse scale
    prediction_scaled = model.predict(X_input)
    prediction = scaler.inverse_transform(prediction_scaled)[0][0]

    return round(prediction, 2)
>>>>>>> ea27301 (git add)
