# AQI Prediction Web App

This **Air Quality Index (AQI) Prediction Web App** leverages real-world air quality data collected from 2019 to 2023 across major Indian cities to predict future AQI values using a deep learning model.

## Overview

Air quality has a significant impact on public health. This app helps citizens make informed decisions by forecasting the AQI based on historical pollution patterns. The model uses a **Long Short-Term Memory (LSTM)** neural network that captures seasonal trends and temporal dependencies in AQI data.

## Features

- Predicts city-wise AQI based on date input
- Provides real-time AQI forecasts
- Uses historical data from 277+ major Indian cities in India
- Displays AQI Category and primary pollutant information

## Data

- Source: [Urban Emissions Website](https://urbanemissions.info/india-air-quality/india-ncap-aqi-indian-cities-2015-2023/)
- Dataset covers January 2019 to December 2023
- Includes City Name, Observation Date, AQI Value, Primary Pollutant, and AQI Category
- Data preprocessing involved handling missing values and normalizing date formats

## Technology Stack

- Backend: Python Flask with LSTM model for AQI prediction
- Frontend: React with CSS3 for UI
- Model: LSTM deep learning model trained on time series AQI data

## Usage

1. Select the city from the dropdown
2. Input the date for which you want the AQI prediction
3. View the predicted AQI and category instantly on the interface

## Project Structure

- `/backend` : Flask API serving the LSTM prediction model
- `/frontend` : React application for user interface

## Explore the Code

- Backend repository: [GitHub - Flask + LSTM Model](https://github.com/toshankanwar/AQI-Prediction/tree/main/backend)
- Frontend repository: [GitHub - React Frontend](https://github.com/toshankanwar/AQI-Prediction/tree/main/frontend)

## Contact

Feedback and collaboration inquiries welcome!  
Email: [contact@toshankanwar.website](mailto:contact@toshankanwar.website)

---

*This tool promotes awareness about air quality and helps citizens make data-driven decisions for health and safety.*
