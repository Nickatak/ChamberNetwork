from django.urls import path
from . import views


app_name = 'instruments'

url_patterns = [
    path('', views.dummy),
    path('/(?P\d+)', views.individual_instrument, name="individual_instrument"),
]