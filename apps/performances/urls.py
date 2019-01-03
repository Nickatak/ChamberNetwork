from django.urls import path, re_path
from . import views

app_name = 'performances'

urlpatterns = [ 
	path('add/', views.add, name="add"),
	path('upcoming/', views.upcoming, name="upcoming"),
	# Note: upcoming will evetually need an re_path
]