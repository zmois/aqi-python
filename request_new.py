# import requests
# import datetime
# import json
# from datetime import date 
# import pandas as pd
# from keys import API_KEYS

# # zip_code = "40204" # input zip code
# # input_date = "2020-06-29"  # input date in YYYY-MM-DD format

# def get_current_data(zip_code, API_KEYS):

#     current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
#     rc = requests.get(current)
#     aqi_today = rc.json
#     df_c = pd.json_normalize(aqi_today)
#     return df_c #aqi_today

# def get_historic_data( zip_code, date_past, API_KEYS):

#     historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=text/csv&zipCode={zip_code}&date={date_past}&distance=25&API_KEY={API_KEYS}'
#     rh = requests.get(historic)
#     aqi_past = rh.json()
#     df_h = pd.json_normalize(aqi_past)
#     return  df_h #aqi_past

# def get_forecast_data(zip_code, tomorrow, API_KEYS):

#     forecast = f'http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zip_code}&date={date_tomorrow}&distance=25&API_KEY={API_KEYS}'
#     rf = requests.get(forecast)
#     aqi_forecast = rf.json()
#     df_f = pd.json_normalize(aqi_forecast)
#     return  df_f #aqi_forecast

# def search_data(zip_code, date_tomorrow, date_past, API_KEYS):
#      if input_date == str(today):
#         get_current_data(zip_code, API_KEYS)

#      elif input_date == str(tomorrow): 
#        get_forecast_data(zip_code, date_tomorrow, API_KEYS)
  
#      else:
#         get_historic_data(zip_code, date_past, API_KEYS)
   
# if __name__ == "__main__":
#     input_date = input("Please choose a date (YYYY-MM-DD format): ")
#     zip_code = input("Please choose a Zip Code (XXXXX): ")

#     today = datetime.date.today()
#     date_past = str(input_date + "T00-0000") # convert the date to the "YYYY-MM-DDT00-0000" format
#     tomorrow = today + datetime.timedelta(days = 1) 
#     date_tomorrow = str(tomorrow) # convert the date to the "YYYY-MM-DDT00-0000" format

# search_data(zip_code, date_tomorrow, date_past, API_KEYS)
# #     search_for_new_book = googlebooks.asks_user_to_search_again()


