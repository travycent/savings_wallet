from django.shortcuts import render
from .models import transaction_types_model,percentage_limits_model,frequency_model,wallet_model,savings_preference_model,transactions_model,savings_target_model
from .import serializers 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from profiles.auth_backend import CustomAuthBackend

# Instantiate the CustomAuthBackend to use its methods
custom_backend = CustomAuthBackend()
class TransactionTypesApi(APIView):
    """
    Args:
        APIView (_type_): _description_
        Used to create Views for the Transaction Types
    """
    def get(self,request,id=""):
        """
        Args:
            request (HTTP): Allow URLS
            id (any): ID for a Specific Item

        Returns:
            HTTP Response
        """
        if not id: 
            try:
                queryset = transaction_types_model.objects.all().order_by('created_on')
                serializer_class = serializers.TransactionTypeSerializer(queryset, many=True)
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': serializer_class.data,
                }
                return Response(response,status=status_code)
            except Exception as e:
                status_code = status.HTTP_400_BAD_REQUEST
                message = "Sorry, there was an error: {}".format(str(e))
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': message,
                }
                return Response(response,status=status_code)
        elif id:
            try:
                queryset = transaction_types_model.objects.filter(transaction_type_id=id)
                serializer_class = serializers.TransactionTypeSerializer(queryset, many=True)
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': serializer_class.data,
                }
                return Response(response,status=status_code)
            except Exception as e:
                status_code = status.HTTP_400_BAD_REQUEST
                message = "Sorry, there was an error: {}".format(str(e))
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': message,
                }
                return Response(response,status=status_code)
    def post(self, request,id):
        # Return Method Not Allowed (405) response for POST
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        message = "Method not allowed."
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)
    def put(self, request, id):
        # Return Method Not Allowed (405) response for PUT
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        message = "Method not allowed."
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)
 
class PercentageLimitApi(APIView):
    """
    Args:
        APIView (View): 
        Used to create Views for the Percentage Limits
    """
    def get(self,request,id=""):
        """
        Args:
            request (HTTP): Allow URLS
            id (any): ID for a Specific Item

        Returns:
            HTTP Response
        """
        if not id: 
            try:
                queryset = percentage_limits_model.objects.all().order_by('created_on')
                serializer_class = serializers.PercentageLimitSerializer(queryset, many=True)
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': serializer_class.data,
                }
                return Response(response,status=status_code)
            except Exception as e:
                status_code = status.HTTP_400_BAD_REQUEST
                message = "Sorry, there was an error: {}".format(str(e))
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': message,
                }
                return Response(response,status=status_code)
        elif id:
            try:
                queryset = percentage_limits_model.objects.filter(percentage_id=id)
                serializer_class = serializers.PercentageLimitSerializer(queryset, many=True)
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': serializer_class.data,
                }
                return Response(response,status=status_code)
            except Exception as e:
                status_code = status.HTTP_400_BAD_REQUEST
                message = "Sorry, there was an error: {}".format(str(e))
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': message,
                }
                return Response(response,status=status_code)
    def post(self, request,id):
        # Return Method Not Allowed (405) response for POST
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        message = "Method not allowed."
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)
    def put(self, request, id):
        # Return Method Not Allowed (405) response for PUT
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        message = "Method not allowed."
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)

class FrequencyApi(APIView):
    """
    Args:
        APIView (View): 
        Used to create Views for the Frequencies
    """
    def get(self,request,id=""):
        """
        Args:
            request (HTTP): Allow URLS
            id (any): ID for a Specific Item

        Returns:
            HTTP Response
        """
        if not id: 
            try:
                queryset = frequency_model.objects.all().order_by('created_on')
                serializer_class = serializers.FrequencySerializer(queryset, many=True)
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': serializer_class.data,
                }
                return Response(response,status=status_code)
            except Exception as e:
                status_code = status.HTTP_400_BAD_REQUEST
                message = "Sorry, there was an error: {}".format(str(e))
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': message,
                }
                return Response(response,status=status_code)
        elif id:
            try:
                queryset = frequency_model.objects.filter(frequency_id=id)
                serializer_class = serializers.FrequencySerializer(queryset, many=True)
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'data': serializer_class.data,
                }
                return Response(response,status=status_code)
            except Exception as e:
                status_code = status.HTTP_400_BAD_REQUEST
                message = "Sorry, there was an error: {}".format(str(e))
                response = {
                    'success': False,
                    'status_code': status_code,
                    'message': message,
                }
                return Response(response,status=status_code)
    def post(self, request,id):
        # Return Method Not Allowed (405) response for POST
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        message = "Method not allowed."
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)
    def put(self, request, id):
        # Return Method Not Allowed (405) response for PUT
        status_code = status.HTTP_405_METHOD_NOT_ALLOWED
        message = "Method not allowed."
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)
    
@api_view(['GET'])
def get_customer_wallet(request,userId=""):
    """
        Args:
            request (HTTP): Allow URLS
            user (any): Email for a Specific User

        Returns:
            HTTP Response
    """
    if not userId or userId =="":
        status_code = status.HTTP_400_BAD_REQUEST
        message = "UserId is Required"
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response,status=status_code)
    
    try:
        # Get User ID
        user =  custom_backend.get_user_id_by_email(userId).pk
        
        # queryset = wallet_model.objects.all().order_by('wallet_update_date')
        queryset = wallet_model.objects.filter(user=user)
        serializer_class = serializers.WalletSerializer(queryset, many=True)
        status_code = status.HTTP_200_OK
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code)    
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Sorry, there was an error: {}".format(str(e))
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response,status=status_code)
@api_view (['GET'])
def get_customer_transactions(request, userId = ""):
    if not userId or userId =="":
        status_code = status.HTTP_400_BAD_REQUEST
        message = "UserId is Required"
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response,status=status_code) 
    try:
        # Get User ID
        user =  custom_backend.get_user_id_by_email(userId).pk
        # queryset = transactions_model.objects.all().order_by('transaction_date')
        queryset = transactions_model.objects.filter(user=user).order_by('-transaction_date')
        status_code = status.HTTP_200_OK
        serializer_class = serializers.UserTransactionSerializer(queryset, many=True)
        response = {
            'success' : 'True',
            'status_code' : status_code,
            'data': serializer_class.data,
        }
        return Response(response,status=status_code) 
        
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Sorry, there was an error: {}".format(str(e))
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response,status=status_code)   
@api_view (['POST'])
def create_customer_transaction(request,userId=""):
    """
        Args:
            request (HTTP): Allow URLS
            user (any): Email for a Specific User

        Returns:
            HTTP Response
    """
    if not userId or userId =="":
        status_code = status.HTTP_400_BAD_REQUEST
        message = "UserId is Required"
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response,status=status_code)  
    try:
        # Get User ID
        user =  custom_backend.get_user_id_by_email(userId).pk
        
        message = "UserId is Required"
        status_code = status.HTTP_400_BAD_REQUEST
        response = {
            'success': False,
            'status_code': status_code,
            'message': user,
        }
        return Response(response,status=status_code) 
        
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Sorry, there was an error: {}".format(str(e))
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response,status=status_code)
         

                

