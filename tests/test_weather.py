import unittest
import responses
import weather


API_KEY = 'e7d99fbae935d84dafae9ba51bc49270'
DEFAULT_WEATHER_UNITS = 'imperial'
WEATHER_URL = 'https://api.openweathermap.org/data/2.5/weather'


class TestWeatherAPI(unittest.TestCase):

    @responses.activate
    def test_weather_by_zip(self):
        """
        Given a zip code, make a sucessful request
        """
        url = WEATHER_URL + "?zip={}&APPID={}".format(
            23602,
            API_KEY
        )

        responses.add(
            responses.GET,
            url,
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

        url = WEATHER_URL + "?zip={}&APPID={}".format(
            12345,
            API_KEY
        )

        responses.add(
            responses.GET,
            url,
            status=404,
            json={'error': 'city not found'}
        )

        res = weather.fetch_weather(12345)

        self.assertEqual(res[0], 404)
        self.assertEqual(res[1], {u'error': u'city not found'})
