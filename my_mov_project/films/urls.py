from django import forms
from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    path('', views.films, name='films'),
    path('film/<int:film_id>', views.film, name='film'),
    path('add/', views.add_film, name='add_film')
]