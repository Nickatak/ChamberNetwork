from django.urls import path
from . import views


app_name = 'instruments'

url_patterns = [
    path('', views.dummy),
]