import unittest

import weather

from mock import Mock, MagicMock, patch

import responses
import requests




class TestWeatherAPI(unittest.TestCase):

    @responses.activate
    def test_weather_by_zip(self):
        """
        Given a zip code, make a sucessful request
        """
        url = weather.weather.WEATHER_URL
        responses.add(
            responses.GET,
            'https://api.openweathermap.org/data/2.5/weather?units=imperial&zip=23602&APPID=e7d99fbae935d84dafae9ba51bc49270',
            status=200,
            body={}
        )

        res = weather.fetch_weather(23602)

        self.assertEqual(res[0], 200)
        self.assertEqual(res[1], {})

    @responses.activate
    def test_weather_by_zip_4xx(self):
        """
        Given a zip code, fail the request
        """
        url = weather.weather.WEATHER_URL
        responses.add(
            responses.GET,
            'https://api.openweathermap.org/data/2.5/weather?units=imperial&zip=12345&APPID=e7d99fbae935d84dafae9ba51bc49270',
            status=404,
            json={'error': 'city not found'}
        )

        res = weather.fetch_weather(12345)

        self.assertEqual(res[0], 404)
        self.assertEqual(res[1], {u'error': u'city not found'})
