from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class  HelloApiView(APIView):
    """Test api"""

    def get(self, request, format=None):
        """Retorna lista de funcoes"""

        an_apiview = [
            'Uses HTTP methods as function',
            'Its is similar to a tradicional Djanfo view',
            'Gives you the most conrol over your logic',
            'Is mapped manually tourls'
        ]

        return Response({'message' : 'Hello', 'an_apiview' : an_apiview})
