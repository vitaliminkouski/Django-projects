from django.http import HttpResponse
from django.shortcuts import render

def index(request):
     return HttpResponse('Women application page')

def cats(request, cat_id):
     return HttpResponse(f'<h1>Articles by categories</h1><p> cat_id: {cat_id}</p>')

def cats_by_slugs(request, cat_slug):
     return HttpResponse(f'<h1>Articles by categories</h1> <p>cat_slug: {cat_slug}</p>')

def archive(request, year):
     return HttpResponse(f'<h1>Archives by year</h1> <p>year: {year}</p>')