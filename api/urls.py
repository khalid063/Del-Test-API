from django.urls import path
from .views import get_users, login_user, register_user

urlpatterns = [
    path('login/', login_user, name='login_user'),
    path('users/', get_users, name='get_users'),
    #path('users/', get_user, name='get_user'),               # It is a Test API 
    path('register', register_user, name='register_user'),         # User Registration url
    # path('login/', login_user, name='login_user'),           # User Login API url
]
