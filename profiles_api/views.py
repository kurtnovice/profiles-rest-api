from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """docstring for ."""

    def get(self, request, format = None):
        """returns a list of API views"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)'
            'Is similar to a traditional Django view'
            'Is mapped manually to URLS'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
