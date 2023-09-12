from django.contrib.auth import get_user_model
#Import all the models
from .models import UsersModel
from rest_framework import views, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseForbidden

from .serializers import LoginSerializer,UserSerializer
from .authentication import JWTAuthentication

User = get_user_model()

class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        email_or_phone_number = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = UsersModel.objects.filter(email=email_or_phone_number).first()
        serializer_class=UserSerializer(user)
        if user is None:
            user = UsersModel.objects.filter(phone_number=email_or_phone_number).first()
            

        if user is None or not user.check_password(password):
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

        # Generate the JWT token
        jwt_token = JWTAuthentication.create_jwt(user)

        return Response({'token': jwt_token,'user_data' : serializer_class.data})