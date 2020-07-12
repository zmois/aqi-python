import requests
import datetime
import json
from datetime import date 
import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt
from keys import API_KEYS

def get_current_data(zip_code, API_KEYS):

    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    aqi = requests.get(current).json()
    #df = pd.json_normalize(aqi)
    # plot_today = df_c[['ReportingArea', 'StateCode', 'DateObserved', 'ParameterName', 'AQI', 'Category.Name']]
    # plot_today.to_csv('data/c_modified.csv')
    return aqi

def get_historic_data(zip_code, date_past, API_KEYS):

    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zip_code}&date={date_past}&distance=25&API_KEY={API_KEYS}'
    aqi = requests.get(historic).json()
    # df_h = pd.json_normalize(aqi_past)
    # plot_historic = df_h[['ReportingArea', 'StateCode', 'DateObserved', 'ParameterName', 'AQI', 'Category.Name']]
    # plot_historic.to_csv('data/h_modified.csv')
    return aqi

def get_forecast_data(zip_code, date_tomorrow, API_KEYS):

    forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
    aqi_f = requests.get(forecast).json()
    # df_f = pd.json_normalize(aqi_forecast)
    # plot_forecast = df_f[['ReportingArea', 'DateForecast', 'ParameterName', 'Category.Name']]
    # plot_forecast.to_csv('data/f_modified.csv')
    return  aqi_f

def search_data(input_date, zip_code, date_tomorrow, date_past, API_KEYS):
    if input_date == str(today):
        current_data = get_current_data(zip_code, API_KEYS)
        return current_data 

    elif input_date == date_tomorrow: 
       forecast_data = get_forecast_data(zip_code, date_tomorrow, API_KEYS)
       return forecast_data 

    else:
        past_data = get_historic_data(zip_code, date_past, API_KEYS)
        return past_data 

def store_data_to_df(data):
    df = pd.json_normalize(data)
    data_to_plot = df[['ReportingArea', 'StateCode', 'DateObserved', 'ParameterName', 'AQI', 'Category.Name']]
    # plot_data.to_csv('data/modified.csv')
    return data_to_plot

def store_data_f_to_df(data):
    df = pd.json_normalize(data)
    data_to_plot_f = df[['ReportingArea', 'DateForecast', 'ParameterName', 'Category.Name']]
    # plot_data.to_csv('data/f_modified.csv')
    return data_to_plot_f
 
def save_to_file(data_to_plot, file_name):
    stf = data_to_plot.to_csv(f'results/{file_name}')
    return stf

def plot_data(input_date):
    plt.style.use("fivethirtyeight")
    data = pd.read_csv(f'results/{input_date}')
    x = data['ParameterName']
    y = data['AQI']
    plt.bar(x, y)
    plt.title("AirNow")
    plt.xlabel("AQI")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()   
    
def plot_data_f(input_date):
    plt.style.use("fivethirtyeight")
    data = pd.read_csv(f'results/{input_date}')
    x = data['ParameterName']
    y = data['Category.Name']
    plt.bar(x, y)
    plt.title("AirNow")
    plt.xlabel("AQI")
    plt.ylabel("Value")
    plt.tight_layout()
    plt.show()  

# def asks_user_to_search_again(self):
#     search_again = input("Would you like to search again? Enter y for Yes and n for No:")
#     user_wants_search_again = search_again == 'y'
#     if user_wants_search_again:
#         new_input_date = input("Please choose a date (YYYY-MM-DD format): ")
#         new_date_search = self.store_search(new_input_date)
#         new_zip_code = input("Please choose a Zip Code (XXXXX): ")
#         new_zip_code_search =  self.store_search(new_zip_code)
#         new = self.displays_dataframe(new_result)
#         print(new_result)
#     else:
#         print("Have a good day!")


if __name__ == "__main__":
    input_date = input("Please choose a date (YYYY-MM-DD format): ")
    zip_code = input("Please choose a Zip Code (XXXXX): ")

    today = datetime.date.today()
    date_past = str(input_date + "T00-0000") # convert the date to the "YYYY-MM-DDT00-0000" format
    tomorrow = today + datetime.timedelta(days = 1) 
    date_tomorrow = str(tomorrow) # convert the date to the "YYYY-MM-DDT00-0000" format
    
    data = search_data(input_date, zip_code, date_tomorrow, date_past, API_KEYS)
    # print(data)

    if input_date == str(tomorrow): 
       data_frame_f = store_data_f_to_df(data)
       to_file = save_to_file(data_frame_f, input_date) 
       print(data_frame_f)
       plot_data_f(input_date)
    else:
        data_frame = store_data_to_df(data)
        to_file = save_to_file(data_frame, input_date)
        print(data_frame)
        plot_data(input_date)
        


    