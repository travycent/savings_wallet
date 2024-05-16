from rest_framework import serializers #import the serializer
from .models import UsersModel
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    date_joined = serializers.DateTimeField(read_only=True, required=False)
    user_image = serializers.ImageField(allow_null=True, required=False)
    
    def create(self, validated_data):
        return UsersModel.objects.create(**validated_data)
        # # user = UsersModel.objects.create(**validated_data)
        # # if 'password' in validated_data:  # Check if password is provided
        # #     user.set_password(validated_data['password']) 
        # user = UsersModel(**validated_data)
        # if 'password' in validated_data:  # Check if password is provided
        #     print(validated_data['password'])
        #     validated_data['password'] = make_password(validated_data['password'])
        #     print(validated_data['password'])
        #     # user.set_password(validated_data['password'])  # Set password using set_password()
        # user.save()  # Save the user object
        # return user
    class Meta:
        model = UsersModel
        fields = ['id','password','nin','email','phone_number','first_name','last_name','user_image','date_joined']
        