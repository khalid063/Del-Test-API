from sqlite3 import IntegrityError
from django.shortcuts import render # type: ignore
from api.models import CustomUser
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .serializer import RegistrationSerializer, UserSerializer
from django.db.utils import IntegrityError # type: ignore
from rest_framework import generics # type: ignore

from rest_framework import status # type: ignore

from django.contrib.auth import authenticate # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore # Correct import
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse("Welcome to the Delta API!")


# ///--------------------------------------------- Test API -------------------------------------------------------------------///

@api_view(['GET'])
def get_users(request):
    users = CustomUser.objects.all()  # Fetch all users from the database
    print(users)
    return Response({"users": users})

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    user = authenticate(username=username, password=password)
    
    if user is not None:
        # Get or create the token for the user
        token, created = Token.objects.get_or_create(user=user)
        
        # Prepare the response data with user profile and token
        user_data = {
            'username': user.username,
            'name': user.name,
            'phone_number': user.phone_number,
            'token': token.key,
        }
        
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)



""" ---------------------------------------------- Registration of User -------------------------------------------------------- """
""" ---------------------------- Registration of User --------------------------- """

@api_view(['POST', 'GET'])  # Allow both POST and GET requests
def register_user(request):
    if request.method == 'POST':
        print("call this view ")
        serializer = RegistrationSerializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()  # Try to save the user
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except IntegrityError as e:
                if 'UNIQUE constraint failed' in str(e):
                    return Response(
                        {"error": "A user with this username already exists."},
                        status=status.HTTP_400_BAD_REQUEST
                    )
                return Response(
                    {"error": "An error occurred during registration."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        return Response({"message": "GET request for register_user endpoint."})
    

# ------------------------------- get "Registrar User List" ------------------------------///
@api_view(['GET'])
def get_registrar_users_list(request):
    customUserList = CustomUser.objects.all()
    serializer = RegistrationSerializer(customUserList, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def register_user(request):
#     serializer = RegistrationSerializer(data=request.data)

#     if serializer.is_valid():
#         try:
#             serializer.save()  # Try to save the user
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         except IntegrityError as e:
#             # Handle the IntegrityError for duplicate username
#             if 'UNIQUE constraint failed' in str(e):
#                 return Response(
#                     {"error": "A user with this username already exists."},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
#             return Response(
#                 {"error": "An error occurred during registration."},
#                 status=status.HTTP_400_BAD_REQUEST
#             )
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



















# # ///---------------------------------------------- Login API for User ---------------------------------------///
# @api_view(['POST'])
# def login_user(request):
#     username = request.data.get('username')
#     password = request.data.get('password')
    
#     user = authenticate(username=username, password=password)
    
#     if user is not None:
#         # Get or create the token for the user
#         token, created = Token.objects.get_or_create(user=user)
        
#         # Prepare the response data with user profile and token
#         user_data = {
#             'username': user.username,
#             'name': user.name,
#             'phone_number': user.phone_number,
#             'token': token.key,
#         }
        
#         return Response(user_data, status=status.HTTP_200_OK)
#     else:
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
