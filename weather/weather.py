import requests
import pprint

from flask import Flask


API_KEY = 'e7d99fbae935d84dafae9ba51bc49270'
DEFAULT_WEATHER_UNITS = 'imperial'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'


def fetch_weather(location, units=None):
    """
    Given a location, return the current weather in that location
    """

    payload = {
        'APPID': API_KEY,
        'zip': location ,
        'units': units or DEFAULT_WEATHER_UNITS
    }

    resp = requests.get(WEATHER_URL, params=payload)

    return resp.status_code, resp.json()
