from django.urls import path
from .  import views

# All functional views go here.
urlpatterns = [
    path('register_member/', views.register_member),
    path('register_patron/', views.register_patron),
    path('register_coach/', views.register_coach),
    path('login_handler/', views.process_login),
]