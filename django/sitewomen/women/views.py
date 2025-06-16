from django.db.models.signals import post_save
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.template.defaultfilters import join
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from .models import Women, Category, TagPost, UploadFiles
from .forms import AddPostForm, UploadFileForm

menu=[
    {'title': 'Contacts', 'url_name': 'contacts'},
    {'title': 'Add Page', 'url_name': 'add_page'},
    {'title': 'Log in', 'url_name': 'login'},
    {'title': 'About', 'url_name': 'about'},
]


# def index(request):
#     posts=Women.published.all().select_related('cat')
#     data={'title': 'Main page',
#           'menu': menu,
#           'posts': posts ,
#           'cat_selected': 0,
#           }
#     return render(request, 'women/index.html', data)

class WomenHome(ListView):
    model=Women
    template_name = 'women/index.html'

    context_object_name = 'posts'
    extra_context = {
          'title': 'Main page',
          'menu': menu,
          'cat_selected': 0,
          }

    def get_queryset(self):
        return Women.published.all().select_related('cat')



# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

def about(request):
    if request.method=='POST':
        form=UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp=UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form=UploadFileForm()
    data = {'title': 'About web-site', 'menu': menu, 'form': form}
    return render(request, 'women/about.html', data)


def contacts(request):
    return HttpResponse('<h1>Contact info</h1>')

# def add_page(request):
#     if(request.method=='POST'):
#         form=AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form=AddPostForm()
#
#     data={
#         'menu': menu,
#         'title': 'Adding page',
#         'form': form,
#     }
#     return render(request, 'women/addpage.html', data)

# class AddPage(View):
#     def get(self, request):
#         form=AddPostForm()
#
#         data = {
#             'menu': menu,
#             'title': 'Adding page',
#             'form': form,
#         }
#         return render(request, 'women/addpage.html', data)
#
#     def post(self, request):
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#
#         data = {
#             'menu': menu,
#             'title': 'Adding page',
#             'form': form,
#         }
#         return render(request, 'women/addpage.html', data)

class AddPage(CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')

    extra_context = {
        'title': 'Adding a page',
        'menu': menu,
        'action_to_do': 'Add'
    }

class UpdatePage(UpdateView):
    model=Women
    fields = ['title', 'content', 'photo', 'cat', 'husband', 'tags']
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    extra_context = {
        'title': 'Editing a page',
        'menu': menu,
        'action_to_do': 'Update'
    }




def login(request):
    return render(request, 'women/login.html')



# def show_post(request, post_slug):
#     post=get_object_or_404(Women, slug=post_slug)
#
#     data={
#         'title': post.title,
#         'menu': menu,
#         'post': post,
#         'cat_selected': 1,
#     }
#     return render(request, 'women/post.html', context=data)

class ShowPost(DetailView):
    # model=Women
    template_name='women/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['title']=context['post'].title
        context['menu']=menu

        return context

    def get_object(self, queryset=None):
        return get_object_or_404(Women.published, slug=self.kwargs[self.slug_url_kwarg])


# def show_category(request, cat_slug):
#     category=get_object_or_404(Category, slug=cat_slug)
#     posts=Women.published.filter(cat_id=category.pk).select_related('cat')
#
#     data = {'title': f'Category: {category.name}',
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': category.pk,
#             }
#     return render(request, 'women/index.html', context=data)

class WomenCategory(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        cat=context['posts'][0].cat
        context['title']='Category - '+cat.name
        context['menu']=menu
        context['cat_selected']=cat.id
        return context





# def show_tag_postlist(request, tag_slug):
#     tag=get_object_or_404(TagPost, slug=tag_slug)
#     posts=tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related()
#
#     data = {'title': f'Tag: {tag.tag}',
#             'menu': menu,
#             'posts': posts,
#             'cat_selected': None,
#             }
#     return render(request, 'women/index.html', context=data)

class TagPostList(ListView):
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.published.filter(tags__slug=self.kwargs['tag_slug']).select_related

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        tag=TagPost.objects.get(slug=self.kwargs['tag_slug'])
        context['title']='Tag '+ tag.tag
        context['menu']=menu
        context['cat_selected']=0
        return context

def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')

