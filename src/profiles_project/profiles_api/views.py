from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers

# Create your views here.

class  HelloApiView(APIView):
    """Test api"""

    serializer_class = serializers.HelloSerealizer

    def get(self, request, format=None):
        """Retorna lista de funcoes"""

        an_apiview = [
            'Uses HTTP methods as function',
            'Its is similar to a tradicional Djanfo view',
            'Gives you the most conrol over your logic',
            'Is mapped manually tourls'
        ]

        return Response({ 'message' : 'Hello', 'an_apiview' : an_apiview})

    def post(self, request):
        """Create a hello message with our name."""
        serializer = serializers.HelloSerealizer(data=request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
