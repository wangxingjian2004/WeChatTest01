# -*- coding: utf-8 -*-
import requests
import sys
sys.path.append("..")
from utils.const_value import WEATHER_DEFAULT_API, WEATHER_DEFAULT_LANGUAGE, WEATHER_DEFAULT_UNIT, WEATHER_KEY, CITIES_EXCEL
from utils.excel import Excel

class Weather(object):
    def __init__(self, locationStr):
        self.__locationStr = locationStr

    def parse_location_str(self):
        excel = Excel(CITIES_EXCEL)
        cities = excel.get_data_by_name(name=u'中国地级市', row_start=1, col_start=1, row_end=9999, col_end=1)
        for city in cities:
            if city[0] in self.__locationStr:
                self.__location = city
                break

    def fetchWeather(self):
        self.parse_location_str()
        result = requests.get(WEATHER_DEFAULT_API, params={
            'key' : WEATHER_KEY,
            'location' : self.__location,
            'language' : WEATHER_DEFAULT_LANGUAGE,
            'unit' : WEATHER_DEFAULT_UNIT
        }, timeout=1)
        return result.text.encode('utf-8')

if __name__ == '__main__':
    weather = Weather(u'天气聊城')
    print(weather.fetchWeather())



