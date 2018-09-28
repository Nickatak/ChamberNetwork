from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.add, name="add"),
	path('performances/', views.performances, name="performances"),
	path('calendar/', views.calendar, name="calendar"),
]