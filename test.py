# Create a command-line tool that accepts a city's name and returns the current weather forecast. Leverage OpenWeatherMap API to fetch weather data and parse it using Python.
# Usage: python test.py <city_name>
# Example: python test.py London
# Output: Current weather in London: 10 degrees Celsius, clear sky

import sys
import requests
import json

# API key
api_key = "08e4df6bb7c12b32ed196efb7203383d"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# city_name variable to store the name of city
city_name = sys.argv[1]

# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
x = response.json()

# Now x contains list of nested dictionaries
# Check the value of "cod" key is equal to
# "404", means city is found otherwise,
# city is not found
if x["cod"] != "404":
    
        # store the value of "main"
        # key in variable y
        y = x["main"]
    
        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"]
    
        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]
    
        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]
    
        # store the value of "weather"
        # key in variable z
        z = x["weather"]
    
        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]
    
        # print following values
        print(" Temperature (in kelvin unit) = " +
            str(current_temperature) +
            "\n atmospheric pressure (in hPa unit) = " +
            str(current_pressure) +
            "\n humidity (in percentage) = " +
            str(current_humidity) +
            "\n description = " +
            str(weather_description))

else:
    print(" City Not Found ")

# Output: Current weather in London: 10 degrees Celsius, clear sky

