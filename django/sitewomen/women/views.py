from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse
from django.template.defaultfilters import join

from .models import Women, Category, TagPost
from .forms import AddPostForm

menu=[
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Add Page', 'url_name': 'add_page'},
    {'title': 'Log in', 'url_name': 'login'},
    {'title': 'About', 'url_name': 'about'},
]


def index(request):
    posts=Women.published.all().select_related('cat')
    data={'title': 'Main page',
          'menu': menu,
          'posts': posts ,
          'cat_selected': 0,
          }
    return render(request, 'women/index.html', data)


def about(request):
    data = {'title': 'About web-site', 'menu': menu}
    return render(request, 'women/about.html', data)


def contacts(request):
    return HttpResponse('<h1>Contact info</h1>')

def add_page(request):
    if(request.method=='POST'):
        form=AddPostForm(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                Women.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error adding posts')
    else:
        form=AddPostForm()

    data={
        'menu': menu,
        'title': 'Adding page',
        'form': form,
    }
    return render(request, 'women/addpage.html', data)

def login(request):
    return render(request, 'women/login.html')



def show_post(request, post_slug):
    post=get_object_or_404(Women, slug=post_slug)

    data={
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', context=data)

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_category(request, cat_slug):
    category=get_object_or_404(Category, slug=cat_slug)
    posts=Women.published.filter(cat_id=category.pk).select_related('cat')

    data = {'title': f'Category: {category.name}',
            'menu': menu,
            'posts': posts,
            'cat_selected': category.pk,
            }
    return render(request, 'women/index.html', context=data)

def show_tag_postlist(request, tag_slug):
    tag=get_object_or_404(TagPost, slug=tag_slug)
    posts=tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related()

    data = {'title': f'Tag: {tag.tag}',
            'menu': menu,
            'posts': posts,
            'cat_selected': None,
            }
    return render(request, 'women/index.html', context=data)
