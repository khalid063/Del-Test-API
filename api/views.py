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
