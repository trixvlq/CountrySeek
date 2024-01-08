from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .services import *
async def mainPage(request):
    return render(request, 'CountryInfo/site/index.html')

class Search(View):
    async def get(self,request):
        return render(request, 'CountryInfo/site/search.html')
    async def post(self,request):
        q_text = request.POST.get('q_name')
        data = await get_country(q_text)
        weather = await get_country_weather(q_text)
        desc = await get_county_desc(q_text)
        comparesment = await get_comparesment(data.get('c_currency_key')[0])
        context = desc
        context.update({'comparesment':round(comparesment,2)})
        context.update(data)
        context.update(weather)
        print(context)
        return render(request, 'CountryInfo/site/search.html', context)
# async def search(request):
#     '''вьюшка которая возвращает основную информацию о стране'''
#     if request.method == 'POST':
#         q_text = request.POST.get('q_name')
#         data = await get_country(q_text)
#         # weather = await get_country_weather(data.get('c_capital'))
#         # weather_short = weather.get('weather')[0].get('main')
#         # weather_desc = weather.get('weather')[0].get('description')
#         # weather_temp = weather.get('main').get('temp')
#         # weather_feel = weather.get('main').get('feels_like')
#         # weather_min = weather.get('main').get('temp_min')
#         # weather_max = weather.get('main').get('temp_max')
#         # country_desc = await get_county_desc(q_text)
#         # description = country_desc.get('description')
#         # context = {
#         #     'weather_short': weather_short,
#         #     'weather_desc': weather_desc,
#         #     'weather_temp': weather_temp,
#         #     'weather_feel': weather_feel,
#         #     'weather_min': weather_min,
#         #     'weather_max': weather_max,
#         #     'description':description
#         # }
#         # context.update(data)
#         return render(request, 'CountryInfo/site/search.html', data)