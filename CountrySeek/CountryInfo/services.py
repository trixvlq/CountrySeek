import os
import aiohttp
from serpapi import GoogleSearch


async def get_country(name: str):
    url = f'https://restcountries.com/v3.1/name/{name}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                data = data[0]
                print(data)
                c_name = data.get('name').get('official')
                try:
                    c_capital = data.get('capital')[0]
                except TypeError:
                    c_capital = 'Information not found'
                c_currency_key = list(data.get('currencies'))
                c_currency_name = data.get('currencies').get(c_currency_key[0]).get('name')
                c_currency_symbol = data.get('currencies').get(c_currency_key[0]).get('symbol')
                c_region = data.get('region')
                c_languages = data.get('languages')
                c_latlng = data.get('latlng')
                c_borders = data.get('borders')
                c_map_key = list(data.get('maps'))
                c_map = data.get('maps').get(c_map_key[0])
                c_population = data.get('population')
                c_continents = data.get('continents')
                timezones = data.get('timezones')
                flag_key = list(data.get('flags'))
                flag = data.get('flags').get(flag_key[0])
                return {
                    'c_name': c_name,
                    'c_capital': c_capital,
                    'c_currency_key': c_currency_key,
                    'c_currency_name': c_currency_name,
                    'c_currency_symbol': c_currency_symbol,
                    'c_region': c_region,
                    'c_languages': c_languages,
                    'c_latlng': c_latlng,
                    'c_borders': c_borders,
                    'c_map_key': c_map_key,
                    'c_map': c_map,
                    'c_population': c_population,
                    'c_continents': c_continents,
                    'timezones': timezones,
                    'flag_key': flag_key,
                    'flag': flag,
                }
            else:
                return False


async def get_comparesment(name: str):
    key = os.environ.get('api_currency')

    headers = {'apikey': key}

    url = f'https://api.currencyapi.com/v3/latest/?apikey={key}&currencies={name}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                comparesment = data.get('data').get(name).get('value')
                return comparesment
            else:
                return False


async def get_country_weather(capital: str):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={capital}&appid=cb8801fceffebeb18636363fc0e20105&units=metric'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                weather_short = data.get('weather')[0].get('main')
                weather_desc = data.get('weather')[0].get('description')
                weather_temp = data.get('main').get('temp')
                weather_feel = data.get('main').get('feels_like')
                return {
                    'weather_short': weather_short,
                    'weather_desc': weather_desc,
                    'weather_temp': weather_temp,
                    'weather_feel': weather_feel
                }
            else:
                return False


async def get_county_desc(name: str):
    params = {
        'engine': 'google',
        'q': name,
        'api_key': os.environ.get('serpapi_api')
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    data = {
        'description': result['knowledge_graph'].get('description'),
    }
    return data


async def get_county_map(name: str):
    params = {
        'engine': 'google_images',
        'q': name,
        'api_key': os.environ.get('serpapi_api')
    }
    search = GoogleSearch(params)
    result = search.get_dict()
    data = {
        'map': result.get('suggested_searches')[0].get('thumbnail'),
    }
    return data
