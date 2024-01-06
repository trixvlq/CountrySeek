from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .services import *
async def mainPage(request):
    return render(request, 'CountryInfo/site/index.html')

async def search(request):
    '''вьюшка которая возвращает основную информацию о стране'''
    if request.method == 'POST':
        q_text = request.POST.get("q_name")
        data = await get_country(q_text)
        data = data[0]
        c_name = data.get('name').get('official')
        c_capital = data.get('capital')[0]
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
        weather = await get_country_weather(c_capital)
        weather_short = weather.get('weather')[0].get('main')
        weather_desc = weather.get('weather')[0].get('description')
        weather_temp = weather.get('main').get('temp')
        weather_feel = weather.get('main').get('feels_like')
        weather_min = weather.get('main').get('temp_min')
        weather_max = weather.get('main').get('temp_max')
        context = {
            'weather_short': weather_short,
            'weather_desc': weather_desc,
            'weather_temp': weather_temp,
            'weather_feel': weather_feel,
            'weather_min': weather_min,
            'weather_max': weather_max,
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
        return render(request, 'CountryInfo/site/search.html', context)