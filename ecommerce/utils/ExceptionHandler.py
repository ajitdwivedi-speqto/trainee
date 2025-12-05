from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError, ParseError, NotFound, APIException
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from utils.CustomException import InvalidProductId

def custom_exception_handler(exc, context):
    response= exception_handler(exc, context)
    if response is not None:
        custom_response={
            'Success': False,
            'Error_Type': exc.__class__.__name__,
            'Message': "",
            'Details': None
        }
        if isinstance(exc, ValidationError):
            custom_response['Message']="Input Filed is missing"
            custom_response['Details']=response.data
            response.status_code=status.HTTP_400_BAD_REQUEST
        elif isinstance(exc, ParseError):
            custom_response['Message']="Invalid Data is Entered "
            custom_response['Details']=response.data
            response.status_code=status.HTTP_400_BAD_REQUEST
        elif isinstance(exc, NotFound):
            custom_response['Message']="Product not exist with the given id"
            custom_response['Details']=response.data
            response.status_code=status.HTTP_400_BAD_REQUEST
        elif isinstance(exc, InvalidProductId):      # <--- here
            custom_response['Message'] = str(exc.detail)
            response.status_code = status.HTTP_400_BAD_REQUEST

        else:
            custom_response['Message']="Server Error"
            custom_response['Details']=response.data
            response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        response.data = custom_response

        return response