from django.shortcuts import render
from .views import mars, snickers, kitkat
from django.urls import path

urlpatterns = [
    path('Mars/', mars),
    path('snickers/', snickers),
    path('kirkat/', kitkat),
]