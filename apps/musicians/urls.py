from django.urls import path
from . import views

urlpatterns = [
	path('logout/', views.logout, name="logout"),
	path('musician/', views.musician, name="musician"),
	path('dashboard/', views.dashboard, name="dashboard"),
]