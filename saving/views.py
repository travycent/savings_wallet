from django.shortcuts import render
from .models import transaction_types_model,percentage_limits_model,frequency_model,wallet_model,savings_preference_model,transactions_model,savings_target_model
from .serializers import TransactionTypeSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

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
                serializer_class = TransactionTypeSerializer(queryset, many=True)
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
                serializer_class = TransactionTypeSerializer(queryset, many=True)
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
    def post(self, request):
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
                  

