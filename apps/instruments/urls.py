from django.urls import path, re_path
from . import views


app_name = 'instruments'

urlpatterns = [
    path('', views.dummy),
    re_path('(?P<instrument_id>\d+)', views.individual_instrument, name="individual_instrument"),
]