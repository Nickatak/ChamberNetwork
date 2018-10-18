from django.urls import path
from . import views

urlpatterns = [
	path('welcome/', views.welcome, name="welcome"),
	path('register_member/', views.register_member, name="register_member"),
	path('register_coach/', views.register_coach, name="register_coach"),
	path('register_supporter', views.register_supporter, name="register_supporter"),
	path('about/', views.about, name="about"),
]