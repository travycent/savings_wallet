from django.shortcuts import render
from .models import transaction_types_model,percentage_limits_model,frequency_model,wallet_model,savings_preference_model,transactions_model,savings_target_model
from .import serializers 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from profiles.auth_backend import CustomAuthBackend
from core import functions

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
        # Extract Fields
        transaction_amount = functions.is_empty(request.data.get('transaction_amount'),"transaction_amount") and functions.is_float(request.data.get('transaction_amount'),"transaction_amount")
        transaction_type_name = functions.is_empty(request.data.get('transaction_type_name'),"transaction_type_name") and functions.is_int(request.data.get('transaction_type_name'),"transaction_type_name")
        payee = request.data.get('payee')   
        data = {
            'user': user,
            'transaction_amount': transaction_amount,
            'transaction_type_name': transaction_type_name,
            'payee' : payee,
        }
        item=serializers.UserTransactionSerializer(data=data)
        if item.is_valid():

            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
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
def get_customer_savings_preference(request, userId = ""):
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
        queryset = savings_preference_model.objects.filter(user=user).order_by('-savings_preference_start_date')
        status_code = status.HTTP_200_OK
        serializer_class = serializers.UserSavingsPreferenceSerializer(queryset, many=True)
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
def create_customer_savings_preference(request,userId=""):
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
        # Extract Fields
        frequency = functions.is_empty(request.data.get('frequency'),"frequency") and functions.is_int(request.data.get('frequency'),"frequency")
        percentage = functions.is_empty(request.data.get('percentage'),"percentage") and functions.is_int(request.data.get('percentage'),"percentage")
        transaction_type_name = functions.is_empty(request.data.get('transaction_type_name'),"transaction_type_name") and functions.is_int(request.data.get('transaction_type_name'),"transaction_type_name")
        savings_preference_start_date = functions.is_empty(request.data.get('savings_preference_start_date'),"savings_preference_start_date") and functions.is_date(request.data.get('savings_preference_start_date'),"savings_preference_start_date")
        savings_preference_end_date = functions.is_empty(request.data.get('savings_preference_end_date'),"savings_preference_end_date") and functions.is_date(request.data.get('savings_preference_end_date'),"savings_preference_end_date")  
        functions.is_date_greater(savings_preference_start_date,savings_preference_end_date)
        data = {
            'user': user,
            'frequency': frequency,
            'percentage' : percentage,
            'transaction_type_name': transaction_type_name,
            'savings_preference_start_date' : savings_preference_start_date,
            'savings_preference_end_date' : savings_preference_end_date,
        }
        item=serializers.UserSavingsPreferenceSerializer(data=data)
        if item.is_valid():

            new_item=item.save()
            if new_item:
                status_code = status.HTTP_201_CREATED
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Created successfully',
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
def update_customer_savings_preference(request,userId=""):
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
        # Extract Fields
        saving_preference_id = functions.is_empty(request.data.get('saving_preference_id'),"saving_preference_id") and functions.is_int(request.data.get('saving_preference_id'),"saving_preference_id")
        frequency = functions.is_empty(request.data.get('frequency'),"frequency") and functions.is_int(request.data.get('frequency'),"frequency")
        percentage = functions.is_empty(request.data.get('percentage'),"percentage") and functions.is_int(request.data.get('percentage'),"percentage")
        transaction_type_name = functions.is_empty(request.data.get('transaction_type_name'),"transaction_type_name") and functions.is_int(request.data.get('transaction_type_name'),"transaction_type_name")
        savings_preference_start_date = functions.is_empty(request.data.get('savings_preference_start_date'),"savings_preference_start_date") and functions.is_date(request.data.get('savings_preference_start_date'),"savings_preference_start_date")
        savings_preference_end_date = functions.is_empty(request.data.get('savings_preference_end_date'),"savings_preference_end_date") and functions.is_date(request.data.get('savings_preference_end_date'),"savings_preference_end_date")  
        functions.is_date_greater(savings_preference_start_date,savings_preference_end_date)
        queryset = savings_preference_model.objects.filter(saving_preference_id=saving_preference_id).first()

        data = {
            'user': user,
            'saving_preference_id' : saving_preference_id,
            'frequency': frequency,
            'percentage' : percentage,
            'transaction_type_name': transaction_type_name,
            'savings_preference_start_date' : savings_preference_start_date,
            'savings_preference_end_date' : savings_preference_end_date,
        }
        item=serializers.UserSavingsPreferenceSerializer(queryset,data=data)
        if item.is_valid():

            new_item=item.save()
            if new_item:
                status_code = status.HTTP_200_OK
                response = {
                    'success' : 'True',
                    'status_code' : status_code,
                    'message': 'Record Updated successfully',
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
@api_view(['DELETE'])
def delete_customer_savings_preference(request, savings_preference_id):
    try:
        # Get the instance to delete based on the savings_preference_id
        instance = savings_preference_model.objects.get(saving_preference_id=savings_preference_id)
        if instance:
            # Delete the instance using the serializer's delete method
            serializer = serializers.UserSavingsPreferenceSerializer()
            serializer.delete(instance)
            status_code = status.HTTP_204_NO_CONTENT
            response = {
                'success': 'True',
                'status_code': status_code,
                'message': 'Record Deleted successfully',
            }
            return Response(response, status=status_code)
        else:
            status_code = status.HTTP_404_NOT_FOUND
            response = {
                'success': False,
                'status_code': status_code,
                'message': 'Record not found',
            }
            return Response(response, status=status_code)
    # Handle Item Does Not Exist Exceptiom
    except savings_preference_model.DoesNotExist:
        status_code = status.HTTP_404_NOT_FOUND
        response = {
            'success': False,
            'status_code': status_code,
            'message': 'Record not found',
        }
        return Response(response, status=status_code)
    # Handle the Bad Request Format Exception
    except Exception as e:
        status_code = status.HTTP_400_BAD_REQUEST
        message = "Sorry, there was an error: {}".format(str(e))
        response = {
            'success': False,
            'status_code': status_code,
            'message': message,
        }
        return Response(response, status=status_code)
                

                

