from django.urls import path
from .  import views

# All functional views go here.
urlpatterns = [
    path('process_login/', views.process_login),
]