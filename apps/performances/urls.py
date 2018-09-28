from django.urls import path
from . import views

urlpatterns = [
	path('add/', views.add, name="add"),
	path('performance/', views.performance, name="performance"),
	path('calendar/', views.calendar, name="calendar"),
]