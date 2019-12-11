from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets

# Create your views here.

class HelloApiView(APIView):
    """docstring for ."""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format = None):
        """returns a list of API views"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Is mapped manually to URLS',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message  with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status = status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, pk=None):
        """Handling updating object"""
        return Response({"method": 'PUT'})

    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': "DELETE"})

class HelloViewSet(viewsets.ViewSet):
    """Test viewset api """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """return a hello message"""
        a_viewset = [
            'Uses action (list, create, retrieve, update, partial_update)',
            'Automatically maps to urls using routers',
            'Provides more functionality with less code'
        ]

        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handle getting an object by its id"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating a part of an object"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """removing an object"""
        return Response({'http_method': 'DELETE'})
