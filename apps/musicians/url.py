from django.urls import path
from . import views

urlpatterns = [
	path('welcome/', welcome.main, name="welcome"),
	path('register/', register.main, name="register"),
	path('login/', login.main, name="login"),
	path('logout/', logout.main, name="logout"),
	path('musician/', musician.main, name="musician"),
]