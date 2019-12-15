from rest_framework import status
from rest_framework.views import Response




def JsonAPiResponse(code, data, message):
    return Response(
        {
            "code"      : code, # status.HTTP_200_OK,
            "data"      : data,
            "message"   : message
        }
    )