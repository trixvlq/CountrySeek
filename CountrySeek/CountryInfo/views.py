from django.http import HttpResponse
from django.shortcuts import render

def mainPage(request):
    return render(request, 'CountryInfo/site/index.html')

def search(request):
    if request.method == 'POST':
        q_text = request.POST.get("q_name")
        return HttpResponse(f'<h1>You looked for {q_text}</h1>')