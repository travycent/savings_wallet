from rest_framework import serializers #import the serializer
from .models import UsersModel
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    phone_number = serializers.CharField(source='get_phone_number')

    class Meta:
        model = UsersModel
        fields = ['id','email','phone_number','first_name','last_name','user_image','date_joined']