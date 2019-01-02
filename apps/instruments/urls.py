from django.urls import path
from . import views


app_name = 'instruments'

urlpatterns = [
    path('', views.dummy),
    path('/(?P<instrument_id>\d+)', views.individual_instrument, name="individual_instrument"),
]