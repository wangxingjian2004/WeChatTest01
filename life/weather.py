# -*- coding: utf-8 -*-
import requests
import json
import time

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
            'unit' : WEATHER_DEFAULT_UNIT,
            'start' : 0,
            'days' : 15
        }, timeout=1)
        self.__weather = result.text.encode('utf-8')
        return self.__weather

    def format(self):
        if type(self.__weather) == None:
            pass
        else:
            results = json.loads(self.__weather)
            locationName = results['results'][0]['location']['name']
            lastUpdateDate = results['results'][0]['last_update'].split('T')[0]
            lastUpdateTime = results['results'][0]['last_update'].split('T')[1].split('+')[0]
            formatStr = locationName + '\n'
            daily = results['results'][0]['daily']
            for day in daily:
                date = day['date']
                text_day = day['text_day']
                text_night = day['text_night']
                low = day['low']
                high = day['high']
                wind_scale = day['wind_scale']
                wind_direction = day['wind_direction']
                formatStr += (date + ':' + text_day + '~' + text_night + ' \t' + wind_direction + u'风' + wind_scale + u'级' + '\n')

            formatStr += '\n' + u'当地' + lastUpdateTime + u'更新'

            return formatStr



if __name__ == '__main__':
    weather = Weather(u'天气聊城')
    print(weather.fetchWeather())
    weather.format()



