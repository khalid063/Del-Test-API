from django.urls import path # type: ignore
from .views import get_user

urlpatterns = [
    path('users/', get_user, name='get_user')
]