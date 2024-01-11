from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render
from django.views import View
import asyncio

from .services import *
async def mainPage(request):
    return render(request, 'CountryInfo/site/index.html')

class Search(View):
    async def get(self,request):
        return render(request, 'CountryInfo/site/search.html')
    async def post(self,request):
        q_text = request.POST.get('q_name')
        data, weather, desc, map = await asyncio.gather(
            get_country(q_text),
            get_country_weather(q_text),
            get_county_desc(q_text),
            get_county_map(q_text)
        )

        try:
            if False not in (data, weather):
                comparesment = await get_comparesment(data.get('c_currency_key')[0])
                context = desc
                context.update({'comparesment': round(comparesment, 2)})
                context.update(data)
                context.update(weather)
                context.update(map)
                print(context)
                return render(request, 'CountryInfo/site/search.html', context)
            else:
                return render(request, 'CountryInfo/site/search.html', {'description': 'Bad request'})
        except KeyError:
            raise Http404
# return JsonResponse(context)
