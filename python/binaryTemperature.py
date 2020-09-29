#!/usr/bin/env python3
from pyfirmata import Arduino
from secret import token
import json,requests,sys

def displayToLEDs(decimal_num):
    for i in range(6,1,-1):
        if(decimal_num & 0x01):
            board.digital[i].write(1)
        else:
            board.digital[i].write(0)
        decimal_num = decimal_num >> 1

def getWeather(place):
    # Download the JSON data from OpenWeatherMap.org's API
    url ='http://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (location,token)
    response = requests.get(url)
    response.raise_for_status()

    # Load JSON data into Python variable.
    weatherData = json.loads(response.text)

    # Get temperature
    kelvin = (weatherData['main']['temp'])

    # Convert from Kelvin to Celsius
    celsius = int(kelvin - 273.15)
    return celsius

# Connect to Arduino
port = '/dev/ttyACM0'
board = Arduino(port)
print("Communication Successfully started")

# Get weather data
location = 'Novi Sad'
temperature = getWeather(location)
print('The temperature in %s is:' % (location))
print(str(temperature) + 'C')

# Convert to binary and display on LEDs
displayToLEDs(temperature)

