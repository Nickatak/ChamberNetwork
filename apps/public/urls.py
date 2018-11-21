from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView

app_name = 'public'

urlpatterns = [
    #Index page has no post-fix.
	path('', views.welcome, name="welcome"),
	path('new_member/', views.register_member, name="new_member"),
	path('new_coach/', views.register_coach, name="new_coach"),
	path('new_patron/', views.register_patron, name="new_patron"),
	path('success/', views.success, name="success"),
	path('login/', views.login, name="login"),
	path('logout/', views.logout, name="logout"),
	path('about/', views.about, name="about"),
]