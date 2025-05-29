from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import join

data_db=[
    {'id': 1, 'title': 'Angelina Jolie', 'content': '''<h1>Angelina Jolie biography</h1>
    Angelina Jolie, born on June 4, 1975, in Los Angeles, is an American actress, filmmaker, and humanitarian. She rose to fame with her Oscar-winning performance in Girl, Interrupted (1999) and became widely known for roles in Lara Croft: Tomb Raider, Mr. & Mrs. Smith, and Maleficent. Beyond acting, she has been deeply involved in humanitarian work, serving as a UNHCR Goodwill Ambassador and later as a Special Envoy, completing over 60 field missions. 
    Jolie is also recognized for her advocacy for refugees and displaced people. She has six children and was previously married to actor Brad Pitt, with their divorce finalized in 2024. Jolie remains a prominent figure in both Hollywood and global humanitarian efforts.''',
     'is_published': True},
    {'id': 2, 'title': 'Margo Robbie', 'content': 'Margo Robbie biography', 'is_published': False},
    {'id': 3, 'title': 'J/home/vitali/PycharmProjects/Django-projects/djangoulia Roberts', 'content': 'Julia Roberts biography', 'is_published': True},
]

cats_db=[
    {'id': 1, 'name': 'Actresses'},
    {'id': 2, 'name': 'Singers'},
    {'id': 3, 'name': 'Sportswomen'},
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
          'cat_selected': 0,
          }
    return render(request, 'women/index.html', data)


def about(request):
    data = {'title': 'About web-site', 'menu': menu}
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


def show_category(request, cat_id):
    data = {'title': 'Display by category',
            'menu': menu,
            'posts': data_db,
            'cat_selected': cat_id,
            }
    return render(request, 'women/index.html', context=data)