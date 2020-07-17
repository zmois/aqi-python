# Read Me

This project uses date from www.AirNow.gov - the U.S. Environmental Protection Agency (EPA) AirNow program that provides forecast and real-time observed air quality information across the United States, Canada, and Mexico. AirNow receives real-time air quality observations from over 2,000 monitoring stations and collects forecasts for more than 300 cities.

## Installation & Running

An AirNow API account is required to obtain the API keys and get access to the web services and data feeds. Sign up for an account on the Log In page to get started. https://docs.airnowapi.org/login

**The following Python packages need to be installed:**
- requests
- pandas
- matplotlib 

## Project Overview

The search is performed by Date and Zip Code (aka Reporting Area). Result will be shown as plot for Air Quality Index (AQI)-  levels of ozone, particle pollution, and other common air pollutants on the same scale, the higher the AQI rating, the greater the health impact
• Real-time air quality observations 
• Historical air quality observations 
• Air quality forecasts

**NOTE:** Forecasts are not necessarily available for all reporting areas. In addition, the forecast for each reporting area is unique:
* Forecasts may not be issued every day or may be seasonal (e.g. winter or summer only).
* Forecasts may cover from one to six days.
* Forecasts may cover one or more pollutants (e.g. ozone, PM2.5).
* Forecasts may include an AQI number (e.g., 51) or simply an AQI category (e.g., Moderate or Unhealthy).

## Requirements:

This project fulfills the following requirements:
- Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program
- *Implement a log that records errors, invalid inputs, or other important events and writes them to a text file*
- Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
- Create and call at least 3 functions, at least one of which must return a value that is used
- Connect to an external/3rd party API and read data into your app
- Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)
- Visualize data in a graph, chart, or other visual representation of data

