from django.urls import path
from .views import get_registrar_users_list, get_users, login_user, register_user

urlpatterns = [
    path('register/user-list/', get_registrar_users_list, name='get_registrar_users_list'),
    path('login/', login_user, name='login_user'),
    path('register', register_user, name='register_user'),         # User Registration url
    path('users/', get_users, name='get_users'),
    # path('login/', login_user, name='login_user'),           # User Login API url
]
