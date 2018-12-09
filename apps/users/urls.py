from django.urls import path
from .  import views

# All functional views go here.
urlpatterns = [
    path('login_handler/', views.login_handler, name="login_handler"),
    path('register_member/', views.register_member),
    path('register_patron/', views.register_patron),
    path('dashboard/', views.dashboard),

]

'''
    URLS to be implemented:

    path('logout_handler/', views.logout_handler),
'''