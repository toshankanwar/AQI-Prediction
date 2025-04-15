import pandas as pd
import numpy as np
import tensorflow as tf
import joblib
import os
from datetime import datetime, timedelta

# Model and scaler directories
model_dir = "models"
scaler_dir = "scalers"
sequence_length = 5  # Use past 5 years of AQI data

# AQI data folder
folder_path = "aqi_data/"

def find_city_file(city):
    """Find the correct CSV file for the city."""
    possible_file = os.path.join(folder_path, f"{city}_AQIBulletins.csv")
    if os.path.exists(possible_file):
        return possible_file
    else:
        raise ValueError(f" Data file for city '{city}' not found.")

def load_city_data(city):
    """Load and preprocess AQI data for the given city."""
    file_path = find_city_file(city)
    df = pd.read_csv(file_path)
    df.rename(columns={"date": "Date", "Index Value": "AQI Value"}, inplace=True)
    df["Date"] = pd.to_datetime(df["Date"])
    df.set_index("Date", inplace=True)
    return df.sort_index()

def find_closest_date(df, target_date):
    """Find the closest available date in the dataset for a given target date."""
    if target_date in df.index:
        return target_date
    
    # Find the closest date available
    available_dates = df.index[df.index.month == target_date.month]
    closest_dates = available_dates[available_dates.day == target_date.day]
    
    return closest_dates[-1] if len(closest_dates) > 0 else None

def prepare_input_sequence(df, date, scaler, year_scaler):
    """Prepare the input sequence for the LSTM model, with trend-based estimate fallback."""
    target_date = datetime.strptime(date, "%Y-%m-%d")
    past_values = []

    # Extract AQI values from the same date in the past 5 years
    for i in range(1, sequence_length + 1):
        past_year = target_date.year - i
        past_date = target_date.replace(year=past_year)
        closest_past_date = find_closest_date(df, past_date)

        if closest_past_date is not None:
            past_values.append(df.loc[closest_past_date, "AQI Value"])
        else:
            # ⚠ Trend-based fallback using previous years
            prev_years = [past_year - j for j in range(1, 4) if past_year - j >= df.index.year.min()]
            estimate_values = []
            for y in prev_years:
                try_date = past_date.replace(year=y)
                closest = find_closest_date(df, try_date)
                if closest:
                    estimate_values.append(df.loc[closest, "AQI Value"])
            if estimate_values:
                estimate = np.mean(estimate_values)
                print(f"⚠ Estimating AQI for {past_date.date()} using trend avg: {estimate:.2f}")
                past_values.append(estimate)
            else:
                print(f"⚠ No previous data to estimate for {past_date.date()}. Using last available AQI.")
                past_values.append(df["AQI Value"].iloc[-1])

    # Normalize past values
    past_values = np.array(past_values).reshape(-1, 1)
    past_values_scaled = scaler.transform(past_values).reshape(1, sequence_length, 1)

    # Normalize target year
    target_year_scaled = year_scaler.transform([[target_date.year]]).reshape(1, 1)

    return [past_values_scaled, target_year_scaled]


def predict_aqi(city, date):
    """Predict the AQI for a given city and date."""
    model_path = f"{model_dir}/{city}_model.h5"
    scaler_path = f"{scaler_dir}/{city}_scaler.pkl"
    year_scaler_path = f"{scaler_dir}/{city}_year_scaler.pkl"

    # Check if model and scalers exist
    if not os.path.exists(model_path) or not os.path.exists(scaler_path) or not os.path.exists(year_scaler_path):
        raise ValueError(f" No trained model or scaler found for {city}.")

    # Load city-specific model and scalers
    model = tf.keras.models.load_model(model_path)
    scaler = joblib.load(scaler_path)
    year_scaler = joblib.load(year_scaler_path)

    # Load city data
    df = load_city_data(city)
    X_input = prepare_input_sequence(df, date, scaler, year_scaler)

    # Predict AQI
    predicted_scaled = model.predict(X_input)
    predicted_value = scaler.inverse_transform(predicted_scaled.reshape(-1, 1))[0][0]

    print(f" Predicted AQI for {city} on {date}: {predicted_value:.2f}")
    return predicted_value

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    date = input("Enter date (YYYY-MM-DD): ").strip()

    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format
        predict_aqi(city, date)
    except ValueError as e:
        print(f" Error: {e}")
