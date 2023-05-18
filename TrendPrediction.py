# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:28:06 2023

@author: Andrew
"""


import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Import the datasets
data = pd.read_csv('COVID-19_case_counts_by_date.csv')
full_data = pd.read_csv('COVID-19_case_counts_by_date_Full.csv')

# Convert the dates to pandas datetime format
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)
full_data['Date'] = pd.to_datetime(full_data['Date'])
full_data.set_index('Date', inplace=True)

# Get the COVID-19 case numbers
cases = data['Total_cases']
full_cases = full_data['Total_cases']

# Fit model
model = ARIMA(cases, order=(5,1,0))
model_fit = model.fit()

# Make prediction
start_index = len(cases)
end_index = start_index + 180  # predict the next six months
forecast = model_fit.predict(start=start_index, end=end_index)

# Create a date range for the forecasted data
forecast_dates = pd.date_range(start=cases.index[-1], periods=len(forecast)+1)[1:]

# Plot the actual data
plt.plot(cases.index, cases, color='blue', label='Actual')

# Plot the forecasted data
plt.plot(forecast_dates, forecast, color='red', label='Forecasted')

# Plot the full actual data
plt.plot(full_cases.index, full_cases, color='green', label='Full Actual')

# Set labels and title
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.title('COVID-19 Total Cases Forecast vs Actual')

# Show the legend
plt.legend()

# Show the plot
plt.show()
