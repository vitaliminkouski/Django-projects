from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns=[
    path('', views.index, name='home'),
    path('cats/<int:cat_id>/', views.cats, name='cats_id'),
    path('cats/<slug:cat_slug>/', views.cats_by_slugs, name='cats'),
    path('archive/<year4:year>/', views.archive, name='archieve')
]