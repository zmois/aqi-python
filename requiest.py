import requests
import keys
import datetime
import json
from datetime import date
import pandas as pd

API_KEY = ""
zip_code = "40204" # input zip code
input_date = "2019-06-30"  # input date in YYYY-MM-DD format
today = datetime.date.today()
#print (today)
date = str(input_date + "T00-0000") # convert the date to "2020-06-10T00-0000" format

if input_date == str(today): # if you input today date
    current = f'http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode={zip_code}&distance=25&API_KEY={API_KEYS}'
    rc = requests.get(current)
    aqi_today = rc.text
    print (aqi_today)
   
else: # if you input any other date in the past
    historic = f'http://www.airnowapi.org/aq/observation/zipCode/historical/?format=text/csv&zipCode={zip_code}&date={date}&distance=25&API_KEY={API_KEYS}'
    rh = requests.get(historic)
    aqi_past = rh.text
    print (aqi_past)

# # Calling DataFrame constructor on list 
df = pd.DataFrame(rh) 
print(df) 

