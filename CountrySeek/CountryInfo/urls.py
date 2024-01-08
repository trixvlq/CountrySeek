from django.urls import path
from .views import *

urlpatterns = [
    path('', mainPage, name='MainPage'),
    path('search/', Search.as_view(), name='search'),
]

