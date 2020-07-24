# Read Me

**Code Louisville Python Project**

This project uses date from www.AirNow.gov - the U.S. Environmental Protection Agency (EPA) AirNow program that provides forecast and real-time observed air quality information across the United States, Canada, and Mexico. AirNow receives real-time air quality observations from over 2,000 monitoring stations and collects forecasts for more than 300 cities.

## Technical Summary

- Python 3.8
- Visual Studio Code
- Windows

## Installation

In the beginning, an AirNow API account is required to obtain the API keys and get access to the web services and data feeds. Go to https://docs.airnowapi.org/login and Request an AirNow API Account. Once the account is created, API Keys will be granted. The API key must be saved in keys.py file: *API_KEYS = "XXXXXXXX-XXXX-XXXX-XXXXXXXXXXXX"*

- Clone or Download the project
- Create the virtual environment `python3 -m venv /path/to/new/virtual/environment` (more details here https://docs.python.org/3/library/venv.html)
- Install program dependencies from `requirement.txt` file by typing `pip3 install -r requirements.txt` in the command line
- Open the code in Visual Studio Code and run the code by `python requestAQI.py` command 

OR

If the following Python packages are already installed
   - requests
   - pandas
   - matplotlib
<<<<<<< HEAD
  - seaborn
simply download the requestAQI.py file and run the code by `python requestAQI.py` command.
=======
   - seaborn
 
<<<<<<< HEAD
 then simply download the requestAQI.py file and run the code by 'python requestAQI.py' command.
>>>>>>> 035b8b3f7db4dcf44823f4f9a0dc4697957896df
=======
 then simply download the requestAQI.py file and run the code by `python requestAQI.py` command.
>>>>>>> f375fadc60c47c2fee174d177d19bfaefa91466f

## How to Run 

1. The search is performed by entering the Date and Zip Code. Program starts with the prompt:
**Please choose a date (YYYY-MM-DD format):**
**Please choose a Zip Code (XXXXX):**

- For Real-time air quality observations use today's date as input date
- For Historical air quality observations use any date in the past as input date
- For Air quality forecasts use tomorrow's date as input date

**NOTE:** Forecasts are not necessarily available for all reporting areas. In addition, the forecast for each reporting area is unique:
  * Forecasts may not be issued every day or may be seasonal (e.g. winter or summer only).
  * Forecasts may cover from one to six days.
  * Forecasts may cover one or more pollutants (e.g. ozone, PM2.5).
  * Forecasts may include an AQI number (e.g., 51) or simply an AQI category (e.g., Moderate or Unhealthy).

2. When the search is complited results are saved in the 'results' folder under unique name as the csv files. The Real-time observations and Historical observations are visualized as Seaborn bar plots and saved in the png format. The Forecast observations are represented as table and saved in png format.

3. Program will contunue with the prompt:
**"Would you like to search for different date or Zip Code? Enter y for Yes and n for No:"**
When 'Yes' option is chosen the new search is performed and new search results are saved in the 'results' folder.
But when the 'No' option is chosen program stops with the prompt "Have a good day!"

## Requirements:

This project fulfills the following requirements:
- Implement a “master loop” console application where the user can repeatedly enter
commands/perform actions, including choosing to exit the program
- Create a dictionary or list, populate it with several values, retrieve at least one value, and use it   in your program,
- Read data from an external file, such as text, JSON, CSV, etc and use that data in your application,
- Create and call at least 3 functions, at least one of which must return a value that is used,
- Connect to an external/3rd party API and read data into your app,
- Calculate and display data based on an external factor,
- Visualize data in a graph, chart, or other visual representation of data.
