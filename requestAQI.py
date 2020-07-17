import requests
import datetime
import json
from datetime import date 
import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt
from keys import API_KEYS

'''
   Getting API request for Today date in json format
'''
def get_current_data(zip_code, API_KEYS):

    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    aqi = requests.get(current).json()
    return aqi

'''   
   Getting API request for Historic date in json format
'''
def get_historic_data(zip_code, date_past, API_KEYS):

    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zip_code}&date={date_past}&distance=25&API_KEY={API_KEYS}'
    aqi = requests.get(historic).json()
    return aqi

'''
   Getting API request for Tomorrow date in json format
'''
def get_forecast_data(zip_code, date_tomorrow, API_KEYS):

    forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
    aqi_f = requests.get(forecast).json()
    return  aqi_f

'''
   Searching for the Data depends on the chosen Date
'''
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

'''
   Converting Search Data to Data Frame format for Today and Historic Date
'''
def store_data_to_df(data):

    df = pd.json_normalize(data) 
    df['Location'] = df['ReportingArea'].str.cat(df['StateCode'], sep=", ")
    df.rename(columns = {'DateObserved':'Date','ParameterName':'Air_Pollutants','Category.Name':'Rating'},
              inplace = True)
    data_to_plot = df[['Location','Date','Air_Pollutants','AQI','Rating']]
    # data_to_plot = df[['ReportingArea', 'StateCode', 'DateObserved', 'ParameterName', 'AQI', 'Category.Name']]
    # test_data = df.pivot(index ='Date', columns ='Air_Pollutants', values ='AQI')
    # print(test_data)
    return data_to_plot

'''
   Converting Search Data to Data Frame format for Tomorrow Date
'''
def store_data_f_to_df(data):

    df = pd.json_normalize(data)
    df['Location'] = df['ReportingArea'].str.cat(df['StateCode'], sep=", ")
    df.rename(columns = {'DateForecast':'Forecast_Date','ParameterName':'Air_Pollutants','Category.Name':'Rating'},
              inplace = True)
    data_to_plot_f = df[['Location','Forecast_Date','Air_Pollutants','Rating']]
    # data_to_plot_f = df[['ReportingArea', 'StateCode', 'DateForecast', 'ParameterName', 'Category.Name']]
    # test_data = df.pivot(index ='DateForecast', columns ='ParameterName', values ='Category.Name')
    # print(test_data)
    return data_to_plot_f

'''  
  Saving the Search Data to the csv file
'''
def save_to_file(data_to_plot, file_name):

    stf = data_to_plot.to_csv(f'results/{file_name}.csv')
    return stf

'''
   Plotting Data for Today and Historic Date
'''
def plot_data(input_date):

    data = pd.read_csv(f'results/{input_date}.csv')

    plt.style.use("seaborn-bright")
    # x = data['ParameterName']
    # y = data['AQI']
    # plt.bar(x, y)
    # plt.title("AirNow")
    # plt.xlabel("AQI")
    # plt.ylabel("Value")
    (markerline, stemlines, baseline) = plt.stem(data.Air_Pollutants, data.AQI, use_line_collection=True)
    plt.setp(markerline, markersize=15,markeredgewidth=2)
    plt.setp(stemlines, color = 'grey')
    plt.setp(baseline, visible=False)
    plt.title("Air Quality Index", loc='right')
    plt.xlabel('Air Pollutants')
    plt.ylabel('Value')

    plt.tight_layout()
    # plt.show()   
    plt.savefig(f'results/AQI_{input_date}.png')

'''
   Plotting Data for Tomorrow Date
'''
def plot_data_f(input_date):

    plt.style.use("fivethirtyeight")
    data = pd.read_csv(f'results/{input_date}.csv')
    x = data['Air_Pollutants']
    y = data['Rating']
    plt.bar(x, y)
    plt.title("Air Quality Index")
    plt.xlabel("Air Pollutants")
    plt.ylabel("Value")
    plt.tight_layout()
    # plt.show()  
    plt.savefig(f'results/AQI_{input_date}.png')

'''
   New Search by User
'''
def asks_user_to_search_again(new_input_date, new_zip_code):

    search_again = input("Would you like to search for different date or Zip Code? Enter y for Yes and n for No:")
    user_wants_search_again = search_again == 'y'
    if user_wants_search_again:
        new_input_date = input("Please choose a new date (YYYY-MM-DD format): ")
        new_zip_code = input("Please choose a Zip Code (XXXXX): ")
        new_search = search_data(new_input_date, new_zip_code, date_tomorrow, date_past, API_KEYS)
        # print(new_search)
        return new_search

    else:
        print("Have a good day!")

'''
Main Program
'''    

if __name__ == "__main__":

    input_date = input("Please choose a date (YYYY-MM-DD format): ")
    zip_code = input("Please choose a Zip Code (XXXXX): ")

    today = datetime.date.today()
    date_past = str(input_date + "T00-0000") # Converting the date to the "YYYY-MM-DDT00-0000" format
    tomorrow = today + datetime.timedelta(days = 1) 
    date_tomorrow = str(tomorrow) # Converting the date to the "YYYY-MM-DDT00-0000" format
    data = search_data(input_date, zip_code, date_tomorrow, date_past, API_KEYS)

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

    new_data = asks_user_to_search_again(input_date, zip_code) 
    print (new_data)

else: 

    print("Have a good day!") 
 