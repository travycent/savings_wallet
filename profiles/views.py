from django.contrib.auth import get_user_model
#Import all the models
from .models import UsersModel
from rest_framework import views, permissions, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from django.http import HttpResponseForbidden
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

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
    

class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = UsersModel.objects.all()
    
    @action(detail=True, url_path='all', methods=['get'])
    def user_data(self, request, pk=None):
        if pk is not None:
            # Detail View: Retrieve and return data for a specific user
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        else:
            # List View: Retrieve and return data for all users
            queryset = self.filter_queryset(self.get_queryset())
            serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @action(detail=False, url_path='add', methods=['post'])
    def add_user_data(self, request):
        try:
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                new_item = serializer.save()
                if new_item:
                    status_code = status.HTTP_201_CREATED
                    response = {
                        'success': 'True',
                        'status_code': status_code,
                        'message': 'Record Created successfully',
                    }
                    return Response(response, status=status_code)
            else:
                # Handle serializer errors with a proper response
                status_code = status.HTTP_400_BAD_REQUEST
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': serializer.errors,  # Include specific error details
                }
                return Response(response, status=status_code)
        except Exception as e:
            # Handle unexpected exceptions with a generic error response
            status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
            message = "There was an Error: {}".format(str(e))
            response = {
                'success': False,
                'status_code': status_code,
                'message': message,
            }
            return Response(response, status=status_code)

    
    # @staticmethod
    # @action(detail=True, url_path='user_type', methods=['get'])
    # def user_type_data(request, user_type=None):
    #     if user_type:
    #         try:
    #             queryset = AuthUser.objects.filter(user_type=user_type)
    #             serializer = UserSerializer(queryset, many=True)
    #             return Response(serializer.data, status=status.HTTP_200_OK)
    #         except AuthUser.DoesNotExist:
    #             return Response(status=status.HTTP_404_NOT_FOUND)
    #     return Response({'error': 'User type parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)
    
