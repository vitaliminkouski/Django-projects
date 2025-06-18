from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns=[
    path('', views.WomenHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_page/', views.AddPage.as_view(), name='add_page'),
    path('login/', views.login, name='login'),
    path('category/<slug:cat_slug>/', views.WomenCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.TagPostList.as_view(), name='tag'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    # path('delete/<slug:slug>/', views.DeletePage.as_view(), name='delete_page')
]