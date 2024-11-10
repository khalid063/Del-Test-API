from django.urls import path
from .views import (
    get_user, 
    register_user,
)

urlpatterns = [
    path('users/', get_user, name='get_user'),  # Add comma here
    path('register/', register_user, name='register_user'),  # User Registration url
]






# from django.urls import path # type: ignore
# from .views import (
#     get_user,
#     register_user,
# )

# # urlpatterns = [
# #     path('users/', get_user, name='get_user')
# #     path('register/', register_user, name='register_user'),         # User Registration url
# # ]

# urlpatterns = [
#     path('users/', get_user, name='get_user')   # Missing comma here
#     path('register/', register_user, name='register_user'),  # User Registration url
# ]
