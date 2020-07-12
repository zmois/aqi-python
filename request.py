import requests
from keys import API_KEYS
import datetime
import json
from datetime import date
import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt

zip_code = "40204" # input zip code
input_date = "2020-07-10"  # input date in YYYY-MM-DD format
today = datetime.date.today()
date_past = str(input_date + "T00-0000") # convert the date to "2020-06-10T00-0000" format
tomorrow = today + datetime.timedelta(days = 1) 
date_tomorrow = str(tomorrow) # convert the date to  "YYYY-MM-DDT00-0000" format

if input_date == str(today): # if you input today date
    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    aqi_today = requests.get(current).json()
  
 #  Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_today)
    plot_today = df[['ReportingArea','StateCode','DateObserved','ParameterName','AQI','Category.Name']]
    print(plot_today) 
    plot_today.to_csv('data/t_modified.csv')

elif input_date == str(tomorrow):  # if you input date is tomorrow
    forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
    rf = requests.get(forecast)
    aqi_forecast = requests.get(forecast).json()
    
#  Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_forecast)
    # if not df.empty:      # empty DataFrame 
    plot_forecast = df[['ReportingArea','StateCode','DateForecast','ParameterName','Category.Name']]
    plot_forecast.to_csv('data/f_modified.csv') 
      
    # else:
    #     print("Forecast is not available: ")

else: # if you input any date in the past
    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zip_code}&date={date_past}&distance=25&API_KEY={API_KEYS}'
    aqi_past = requests.get(historic).json()

#    Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_past)
    
    plot_past = df[['ReportingArea','StateCode','DateObserved','ParameterName','AQI','Category.Name']]
    plot_past.to_csv('results/p_modified.csv')

# plotting the AQi data
plt.style.use("fivethirtyeight")
data = pd.read_csv('results/p_modified.csv')
x = data['ParameterName']
y = data['AQI']
plt.bar(x, y)
plt.title("AirNow")
plt.ylabel("Value")
plt.xlabel("AQI")
plt.tight_layout()
plt.show()

  

