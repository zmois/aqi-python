import requests
import datetime
import json
from datetime import date 
import pandas as pd
import csv
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from pandas.plotting import table
from keys import API_KEYS

#   Getting API request for Today date in json format
def get_current_data(zip_code, API_KEYS):

    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    aqi = requests.get(current).json()
    return aqi
  
#   Getting API request for Historic date in json format
def get_historic_data(zip_code, input_date, API_KEYS):

    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=application/json&zipCode={zip_code}&date={input_date}T00-0000&distance=25&API_KEY={API_KEYS}'
    aqi = requests.get(historic).json()
    return aqi

#   Getting API request for Tomorrow date in json format
def get_forecast_data(zip_code, date_tomorrow, API_KEYS):

    forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
    aqi_f = requests.get(forecast).json()
    return  aqi_f

#   Searching for the Data depends on the chosen Date
def search_data(input_date, zip_code, date_tomorrow, API_KEYS):
    if input_date == str(today):
        current_data = get_current_data(zip_code, API_KEYS)
        return current_data 

    elif input_date == date_tomorrow: 
       forecast_data = get_forecast_data(zip_code, date_tomorrow, API_KEYS)
       return forecast_data 

    else:
        past_data = get_historic_data(zip_code, input_date, API_KEYS)
        return past_data 
    
#   Converting Search Data to Data Frame format for Today and Historic Date
def store_data_to_df(data):

    df = pd.json_normalize(data) 
    df['Location'] = df['ReportingArea'].str.cat(df['StateCode'], sep=", ")
    df.rename(columns = {'DateObserved':'Date','ParameterName':'Air_Pollutants','Category.Name':'Rating'},
              inplace = True)
    data_to_plot = df[['Location','Date','Air_Pollutants','AQI','Rating']]
    return data_to_plot

#   Converting Search Data to Data Frame format for Tomorrow Date
def store_data_f_to_df(data):

    df = pd.json_normalize(data)
    df['Location'] = df['ReportingArea'].str.cat(df['StateCode'], sep=", ")
    df.rename(columns = {'DateForecast':'Forecast_Date','ParameterName':'Air_Pollutants','Category.Name':'Rating'},
              inplace = True)
    data_to_plot_f = df[['Location','Forecast_Date','Air_Pollutants','Rating']]
    return data_to_plot_f
  
#   Plotting Data for Today and Historic Date
def plot_data(input_date):

    data = pd.read_csv(f'results/{input_date}-{zip_code}.csv')
    colors = {'Good':'#66BB6A',
              'Moderate':'#FFEB3B',
              'Sensitive':'#F39C12',
              'Unhealthy for Sensitive Groups':'#FF5722',
              'Very Unhealthy':'#8E24AA',
              'Hazardous':'#B71C1C'}
    sns.set(style = "whitegrid")
    g = sns.catplot(x = 'Air_Pollutants', y = 'AQI', hue = 'Rating', data = data, 
                    height = 5, kind ='bar', palette = colors, dodge = False)
    plt.suptitle(f'Air Quality in {data.Location[0]} on {data.Date[0]}')
    g.despine(left=True)
    g.set_ylabels('Rating')
    plt.savefig(f'results/AQI_{input_date}-{zip_code}.png')

#   Save Forecast Date in the Table Format
def plot_data_f(input_date):

    data = pd.read_csv(f'results/{input_date}-{zip_code}.csv')
    data.drop(data.columns[data.columns.str.contains('unnamed',case = False)],axis = 1, inplace = True)
    
    fig, ax = plt.subplots(figsize=(10, 2)) # set size frame
    fig.suptitle(f'Forecast Air Quality')
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    ax.set_frame_on(False)  # no visible frame, uncomment if size is ok
    tb = table(ax, data, loc='upper right', colWidths =  [0.2]*len(data.columns))  # where df is your data frame
    tb.auto_set_font_size(True) # Activate set fontsize manually
    # tb.set_fontsize(16) # if ++fontsize is necessary ++colWidths
    tb.scale(1.5, 1.5) # change size table
    fig.tight_layout()
    plt.savefig(f'results/AQI_{input_date}-{zip_code}.png', transparent = True, bbox_inches='tight', pad_inches=0.1)

#   Saving and visualizing the Data
def data_to_visualize(input_date, zip_code, data):
    if input_date == str(tomorrow): 
       data_frame_f = store_data_f_to_df(data)
       data_frame_f.to_csv(f'results/{input_date}-{zip_code}.csv')
       print(data_frame_f)
       plot_data_f(input_date) 
    else:
        data_frame = store_data_to_df(data)
        data_frame.to_csv(f'results/{input_date}-{zip_code}.csv')
        print(data_frame)
        plot_data(input_date)

#   Main Program
if __name__ == "__main__":

    search_again = 'y'
    while search_again == 'y':

#   Run the Main Loop 
        input_date = input("Please choose a date (YYYY-MM-DD format): ")
        zip_code = input("Please choose a Zip Code (XXXXX): ")
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days = 1) 
        date_tomorrow = str(tomorrow) # Converting the date to the "YYYY-MM-DDT00-0000" format
    
        data = search_data(input_date, zip_code, date_tomorrow, API_KEYS)
        data_to_visualize(input_date, zip_code, data)
   
#   Performming a New Search 
        search_again = input("Would you like to search for different date or Zip Code? Enter y for Yes and n for No:")
 
    print("Have a good day!")
 
