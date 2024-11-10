from rest_framework import serializers # type: ignore
from rest_framework.response import Response # type: ignore
from.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'