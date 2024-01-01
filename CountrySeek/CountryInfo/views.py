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
        return JsonResponse(flag,safe=False)