from django.urls import path
from .  import views

app_name = 'users'

# All functional views go here.
urlpatterns = [
    path('login_handler/', views.login_handler, name="login_handler"),
    path('register_member/', views.register_member, name="member_registration_handler"),
    path('register_patron/', views.register_patron, name="patron_registration_handler"),
    path('dashboard/', views.dashboard, name="dashboard"),

]

'''
    URLS to be implemented:

    path('logout_handler/', views.logout_handler),
'''