from django.urls import path
from . import views

urlpatterns=[
    path('women/', views.index),
    path('cats/', views.cats),
]