from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import join

menu = ['About', 'Add page', 'Get feedback']
data_db=[
    {'id': 1, 'title': 'Andjelina Djoli', 'content': 'Andjelina Djoli biography', 'is_published': True},
    {'id': 2, 'title': 'Margo Robbie', 'content': 'Margo Robbie biography', 'is_published': False},
    {'id': 3, 'title': 'Julia Roberts', 'content': 'Julia Roberts biography', 'is_published': False},
]


def index(request):
    data={'title': 'Main page',
          'menu': join(menu, ' | '),
          'posts': data_db,
          }
    return render(request, 'women/index.html', data)


def about(request):
    data = {'title': 'About web-site'}
    return render(request, 'women/about.html', data)


def cats(request, cat_id):
    return HttpResponse(f'<h1>Articles by categories</h1><p> cat_id: {cat_id}</p>')


def cats_by_slugs(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by categories</h1> <p>cat_slug: {cat_slug}</p>')


def archive(request, year):
    if year > 2025:
        url = reverse('cats', args=('music',))
        return HttpResponseRedirect(url)
    return HttpResponse(f'<h1>Archives by year</h1> <p>year: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
