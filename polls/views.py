from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mars(request):
    return HttpResponse('It is MARS')

def snickers(request):
    return HttpResponse('It is SNICKERS')

def kitkat(request):
    return HttpResponse('It is Kit Kat')
