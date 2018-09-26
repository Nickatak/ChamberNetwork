from django.urls import path
from . import views

urlpatterns = [
	path('welcome/', welcome.main, name="welcome"),
	path('register/', register.main, name="register"),
	path('login/', login.main, name="login"),
]