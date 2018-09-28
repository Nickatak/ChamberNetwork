from django.urls import path
from . import views

urlpatterns = [
	path('welcome/', views.welcome, name="welcome"),
	path('register_member/', views.register_member, name="register_member"),
	path('register_coach/', views.register_coach, name="register_coach"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('musician/', views.musician, name="musician"),
	path('dashboard/', views.dashboard, name="dashboard"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
]