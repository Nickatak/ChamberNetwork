from django.urls import path

from . import views


app_name = 'public'
urlpatterns = [
    #Index page has no post-fix.
	path('', views.welcome, name="welcome"),
	path('new_member/', views.new_member_display, name="new_member"),
	path('new_coach/', views.new_coach_display, name="new_coach"),
	path('new_patron/', views.new_patron_display, name="new_patron"),
	path('success/', views.success, name="success"),
	path('login/', views.login_display, name="login"),
	path('about/', views.about, name="about"),
	path('sponsors/', views.sponsors, name="sponsors"),
	path('resources/', views.resources, name="resources"),
    path('request-reset/', views.pw_reset_display, name='request_reset'),
    path('reset-sent/', views.token_sent, name='reset_sent'),
]
