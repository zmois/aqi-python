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
input_date = "2020-07-17"  # input date in YYYY-MM-DD format
today = datetime.date.today()
date_past = str(input_date + "T00-0000") # convert the date to "2020-06-10T00-0000" format
tomorrow = today + datetime.timedelta(days = 1) 
date_tomorrow = str(tomorrow) # convert the date to  "YYYY-MM-DDT00-0000" format

if input_date == str(today): # if you input today date
    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    aqi_today = requests.get(current).json()
  
 #  Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_today)
    df['Location'] = df['ReportingArea'].str.cat(df['StateCode'], sep=", ")
    df.rename(columns = {'DateObserved':'Date','ParameterName':'Air_Pollutants','Category.Name':'Rating'},
                     inplace = True)
    plot_today = df[['Location','Date','Air_Pollutants','AQI','Rating']]
    # plot_today = df[['ReportingArea','StateCode','DateObserved','ParameterName','AQI','Category.Name']]
    print(plot_today) 
    plot_today.to_csv('results/t_modified.csv')

elif input_date == str(tomorrow):  # if you input date is tomorrow
    forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
    rf = requests.get(forecast)
    aqi_forecast = requests.get(forecast).json()
    
#  Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_forecast)
    plot_forecast = df[['ReportingArea','StateCode','DateForecast','ParameterName','Category.Name']]
    plot_forecast.to_csv('results/f_modified.csv') 
      
   
else: # if you input any date in the past
    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zip_code}&date={date_past}&distance=25&API_KEY={API_KEYS}'
    aqi_past = requests.get(historic).json()
    df = pd.json_normalize(aqi_past)
    # df.to_csv('results/test.csv')
    plot_past = df[['ReportingArea','StateCode','DateObserved','ParameterName','AQI','Category.Name']]
    plot_past.to_csv('results/p_modified.csv')

# plotting the AQI data

# plt.style.use("fivethirtyeight")
# data = pd.read_csv('results/t_modified.csv')
# x = data['Air Pollutants']
# y = data['AQI']
# plt.bar(x, y)
# plt.title("AirNow")
# plt.ylabel("Rating")
# plt.xlabel("Air Pollutants")
# plt.tight_layout()
# plt.show()

test = df.pivot(index='Date', columns='Air_Pollutants', values='AQI') 
test.plot(kind='bar')
plt.tight_layout()
# plt.show()
plt.savefig(f'results/AQI_t_{input_date}.png')
