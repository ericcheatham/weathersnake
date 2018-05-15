import os

import requests
import googlemaps


DEFAULT_WEATHER_UNITS = 'imperial'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'


_gmaps = googlemaps.Client(key=os.environ['GOOGLE_MAPS_API'])


def validate_input(location):
    """
    Validate that we are given a location in the form
    <CITY>,<STATE/COUNTRY>
    """
    return len(location.split(',')) is 2


def get_lat_lon(location):
    """
    Given an address, get the lat and lon back
    """
    res = _gmaps.geocode(location)

    if res:
        res = res[0]
        return res.get('geometry')
    return False


def fetch_weather(location, units=None):
    """
    Given a location, return the current temperature in that location
    """

    if validate_input(location):
        geo = get_lat_lon(location)
        if geo:
            payload = {
                'APPID': os.environ['WEATHER_API'],
                'lat': geo['location']['lat'],
                'lon': geo['location']['lng'],
                'units': units or DEFAULT_WEATHER_UNITS
            }

            resp = requests.get(WEATHER_URL, params=payload)
            return resp.status_code, resp.json()
    return False
