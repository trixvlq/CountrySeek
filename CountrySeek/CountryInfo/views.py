from django.http import HttpResponse, JsonResponse, Http404
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
        try:
            desc = await get_county_desc(q_text)
        except KeyError:
            raise Http404
        if False not in (data,weather):
            comparesment = await get_comparesment(data.get('c_currency_key')[0])
            context = desc
            context.update({'comparesment':round(comparesment,2)})
            context.update(data)
            context.update(weather)
            print(context)
            return render(request, 'CountryInfo/site/search.html', context)
        else:
            return render(request, 'CountryInfo/site/search.html', {
                'description':'Bad request'
            })
# return JsonResponse(context)
