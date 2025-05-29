from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns=[
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.show_post, name='post'),
    path('contacts/', views.contacts, name='contacts'),
    path('add_page/', views.add_page, name='add_page'),
    path('login/', views.login, name='login'),
    path('category/<int:cat_id>/', views.show_category, name='category')
]