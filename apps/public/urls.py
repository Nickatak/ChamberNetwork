from django.urls import path
from . import views
# from django.contrib.auth.views import LoginView

app_name = 'public'

urlpatterns = [
    #Index page has no post-fix.
	path('', views.welcome, name="welcome"),
	path('new_member/', views.new_member_display, name="new_member"),
	path('new_coach/', views.new_member_display, name="new_coach"),
	path('new_patron/', views.new_member_display, name="new_patron"),
	path('success/', views.success, name="success"),
	path('login/', views.login_display, name="login"),
	path('about/', views.about, name="about"),
]