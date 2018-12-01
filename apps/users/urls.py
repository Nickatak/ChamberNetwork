from django.urls import path
from .  import views

# All functional views go here.
urlpatterns = [
    path('login_handler/', views.login_handler, name="login_handler"),
    path('register_member/', views.register_member),
    path('register_patron/', views.register_patron),

]

'''
    URLS to be implemented:
    path('dashboard/', views.dashboard)
    path('register_member/', views.register_member),
    path('register_patron/', views.register_patron),
    path('register_coach/', views.register_coach),

    path('logout_handler/', views.logout_handler),
'''