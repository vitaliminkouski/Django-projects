from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse


def index(request):
     t = render_to_string('women/index.html')
     return HttpResponse(t)

def about(request):
     return render(request, 'women/about.html')

def cats(request, cat_id):
     return HttpResponse(f'<h1>Articles by categories</h1><p> cat_id: {cat_id}</p>')

def cats_by_slugs(request, cat_slug):
     if request.GET:
          print(request.GET)
     return HttpResponse(f'<h1>Articles by categories</h1> <p>cat_slug: {cat_slug}</p>')





def archive(request, year):
     if year>2025:
          url =reverse('cats', args=('music',))
          return HttpResponseRedirect(url)
     return HttpResponse(f'<h1>Archives by year</h1> <p>year: {year}</p>')

def page_not_found(request, exception):
     return HttpResponseNotFound('<h1>Page not found</h1>')