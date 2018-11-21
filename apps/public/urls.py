from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView

app_name = 'public'

urlpatterns = [
    #Index page has no post-fix.
	path('', views.welcome, name="welcome"),
	path('register_member/', views.register_member, name="register_member"),
	path('register_coach/', views.register_coach, name="register_coach"),
	path('register_patron/', views.register_patron, name="register_patron"),
	path('success/', views.success, name="success"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('about/', views.about, name="about"),
]