from django.shortcuts import render
from api.models import User
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .serializer import UserSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
# @api_view(['GET'])
# def get_user(request):
#     return Response(UserSerializer({'name': "Pedro", "age": 23}).data)

@api_view(['GET'])
def get_user(request):
    # Add this permission class if you only need read-only access for unauthenticated users
    permission_classes = [IsAuthenticatedOrReadOnly]

    user = User.objects.all()
    return Response(UserSerializer(user, many=True).data)
