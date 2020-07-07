import requests
from keys import API_KEYS
import datetime
import json
from datetime import date
import pandas as pd

zip_code = "40204" # input zip code
input_date = "2020-07-02"  # input date in YYYY-MM-DD format
today = datetime.date.today()
date_past = str(input_date + "T00-0000") # convert the date to "2020-06-10T00-0000" format
tomorrow = today + datetime.timedelta(days = 1) 
date_tomorrow = str(tomorrow) # convert the date to  "YYYY-MM-DDT00-0000" format

if input_date == str(today): # if you input today date
    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    rc = requests.get(current)
    aqi_today = rc.json()

    with open(f'{input_date}.json', 'w') as f:
        json.dump(aqi_today, f)
   
 #  Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_today)
  
    plot_today = df[['ReportingArea', 'StateCode', 'DateObserved', 'ParameterName', 'AQI', 'Category.Name']]
    print(plot_today) 

elif input_date == str(tomorrow):  # if you input date is tomorrow
    forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
    rf = requests.get(forecast)
    aqi_forecast = rf.json()

    with open(f'{input_date}.json', 'w') as f:
        json.dump(aqi_forecast, f)

    #  Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_forecast)

    plot_forecast = df[['ReportingArea',  'DateForecast', 'ParameterName', 'Category.Name']]
    print(plot_forecast) 

else: # if you input any date in the past
    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zip_code}&date={date_past}&distance=25&API_KEY={API_KEYS}'
    rh = requests.get(historic)
    aqi_past = rh.json()

    with open(f'{input_date}.json', 'w') as f:
        json.dump(aqi_past, f)

    #    Calling DataFrame constructor on list of dict
    df = pd.json_normalize(aqi_past)
    
    plot_past = df[['ReportingArea', 'StateCode', 'DateObserved', 'ParameterName', 'AQI', 'Category.Name']]
    print(plot_past) 

    
 

  

