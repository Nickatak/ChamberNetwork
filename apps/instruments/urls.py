from django.urls import path, re_path

from . import views


app_name = 'instruments'
urlpatterns = [
    re_path('(?P<instrument_id>\d+)', views.individual_display, name="individual_display"),
]
