from django.urls import path
from . import views

urlpatterns = [
	path('instrument/', views.instrument, name="instrument"),
]