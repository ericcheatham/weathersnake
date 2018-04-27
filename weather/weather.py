import requests
import pprint

from flask import Flask


API_KEY = 'e7d99fbae935d84dafae9ba51bc49270'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'
WEATHER_UNITS = 'imperial'


def _process_weather_response(response):
    """
    Given a JSON blob, return the properly formatted weather
    """
    



def fetch_weather(location):
    """
    Given a location, return the current weather in that location
    """

    payload = {
        'APPID': API_KEY,
        'zip': location,
        'units': WEATHER_UNITS
    }

    r = requests.get(WEATHER_URL, params=payload)

    return r.json()
