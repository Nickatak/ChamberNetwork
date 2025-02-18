from django.urls import path, re_path

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
    path('request-reset/', views.request_reset, name='request_reset'),
    path('reset-sent/', views.token_sent, name='reset_sent'),
    path('new_pw_success/', views.new_pw_success, name='new_pw_success'),

    # Below should actually be pw_reset_display.  This'll render the password reset form and then submit it to users:reset-handler
    re_path('reset/(?P<reset_token>[A-Z, a-z, 0-9]{32})/', views.pw_reset_display, name='pw_reset_display'),
]
