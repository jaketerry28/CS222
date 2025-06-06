# assignment4.py

import json
import ssl
from urllib.request import urlopen

MUNCIE_WEATHER_URL = "https://api.weather.gov/points/40.1934,-85.3864"

# to connect to endpoints
def connectEndpoint(url):
    # connect to url
    endPoint = url
    context = ssl._create_unverified_context()
    response = urlopen(endPoint, context=context)
    # load json 
    data = json.loads(response.read())
    return data


def main():
    try:
        # connect to first end point
        cityWeatherURL= connectEndpoint(MUNCIE_WEATHER_URL)

        # grab forecast URL
        forecastURL = cityWeatherURL["properties"]["forecast"]
        #print(forecastURL)

        # connect to forecast URL
        forecastData = connectEndpoint(forecastURL)

        # print out 7 day forecast 
        degrees = chr(176) # get degree sign
        print("Upcoming 7 day forecast in Muncie, Indiana:")
        for event in forecastData["properties"]["periods"]:
            date = event["startTime"].split("T") # split to show dates
            name = event["name"]
            temperature = event["temperature"]
            detailedForecast = event["detailedForecast"]
            print("-------------------------------")
            print(f"{date[0]}: {name}\nTemperature: {temperature}{degrees}F\n\
                  Detailed Forecast: {detailedForecast}")
    except:
        print("Failed to connect")
main()
