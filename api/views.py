from sqlite3 import IntegrityError
from django.shortcuts import render
from api.models import User
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .serializer import ( 
    UserSerializer,
    RegistrationSerializer
)
from rest_framework import status # type: ignore          #*** very importent
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.contrib.auth import authenticate # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore # Correct import

# Create your views here.
# @api_view(['GET'])
# def get_user(request):
#     return Response(UserSerializer({'name': "Pedro", "age": 23}).data)
# ///--------------------------------------------- Test API -------------------------------------------------------------------///
@api_view(['GET'])
def get_user(request):
    # Add this permission class if you only need read-only access for unauthenticated users
    permission_classes = [IsAuthenticatedOrReadOnly]

    user = User.objects.all()
    return Response(UserSerializer(user, many=True).data)


""" ---------------------------------------------- Registration of User -------------------------------------------------------- """
@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)

    if serializer.is_valid():
        try:
            serializer.save()  # Try to save the user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            # Handle the IntegrityError for duplicate username
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

# ///---------------------------------------------- Login API for User ---------------------------------------///
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
