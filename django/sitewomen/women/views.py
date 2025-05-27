from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import join

data_db=[
    {'id': 1, 'title': 'Andjelina Djoli', 'content': 'Andjelina Djoli biography', 'is_published': True},
    {'id': 2, 'title': 'Margo Robbie', 'content': 'Margo Robbie biography', 'is_published': False},
    {'id': 3, 'title': 'Julia Roberts', 'content': 'Julia Roberts biography', 'is_published': True},
]

menu=[
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Add Page', 'url_name': 'add_page'},
    {'title': 'Log in', 'url_name': 'login'},
    {'title': 'About', 'url_name': 'about'},
]


def index(request):
    data={'title': 'Main page',
          'menu': menu,
          'posts': data_db,
          }
    return render(request, 'women/index.html', data)


def about(request):
    data = {'title': 'About web-site'}
    return render(request, 'women/about.html', data)


def contacts(request):
    return HttpResponse('<h1>Contact info</h1>')

def add_page(request):
    return HttpResponse('<h1>Add page</h1>')

def login(request):
    return render(request, 'women/login.html')



def show_post(request, post_id):
    return HttpResponse(f'<h1>post id: {post_id}</h1>')

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
