from django.urls import path, re_path
from .  import views

app_name = 'users'

# All functional views go here.
urlpatterns = [
    path('login_handler/', views.login_handler, name="login_handler"),
    path('logout_handler/', views.logout_handler, name='logout_handler'),
    path('register_coach/', views.register_coach, name="coach_registration_handler"),
    path('register_member/', views.register_member, name="member_registration_handler"),
    path('register_patron/', views.register_patron, name="patron_registration_handler"),
    path('dashboard/', views.dashboard, name="dashboard"),

    re_path('edit_member/(?P<member_id>\d+)/', views.edit_member, name='edit_member'),
    re_path('(?P<member_id>\d+)/', views.individual_member, name="individual_member"),
]