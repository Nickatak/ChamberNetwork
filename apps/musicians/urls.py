from django.urls import path
from . import views

urlpatterns = [
	path('musician/', views.musician, name="musician"),
	path('dashboard/', views.dashboard, name="dashboard"),
]