from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return HttpResponse('Women application page')

def cats(request):
     return HttpResponse('<h1>Articles by categories</h1>')
