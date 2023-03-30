from django.shortcuts import render
from rest_framework.views import APIView
from .ultis import generate_key
import os
from dotenv import load_dotenv
load_dotenv('.env')
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
import requests
from .serializers import AdminKeyTokenSerializer, NormalUserTokenSerializer
from .models import KeyToken

# Create your views here.
text = os.environ['SECRECT_KEY']
salt = bytes(os.environ['SALT_STRING'].encode('utf-8'))
# api_key = os.environ['API_KEY']
iterations = 100000
cipher = generate_key(text, salt, iterations)

class ProxyAPIView(APIView):
    def post(self, request, format=None):
        authorization_header = request.headers.get('Authorization', None)
        auth_key = cipher.decrypt(authorization_header).decode()
        if not (auth_key and KeyToken.objects.filter(api_key=auth_key).exists()):
            return Response({'detail':'Authenticate failed'}, status=status.HTTP_403_FORBIDDEN)
        auth_key = "Bearer "+ auth_key
        host_domain = request.data.pop('host_domain')    
        method = request.data.pop('request_method')
        headers = {'Authorization':auth_key}
        if not (host_domain or method or headers):
            return Response({'detail':'Bad request'}, status=status.HTTP_404_NOT_FOUND)
        data = request.data['body']
        response = requests.request(
            method= method,
            url=host_domain,
            headers=headers,
            json=data,
        )
        return Response(response.json(), status=response.status_code)

class EncryptTokenListView(APIView):
    permission_classes = [permissions.IsAdminUser]
    def get(self, request, format=None):
        query = KeyToken.objects.all()
        serializer = AdminKeyTokenSerializer(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None):
        serializer = AdminKeyTokenSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetEncryptToken(APIView):
    def _get_object(self, hostdomain):
        try:
            return KeyToken.objects.filter(hostdomain__name__icontains=hostdomain).order_by('?').first()
        except KeyToken.DoesNotExist:
            return Response({'detail':'Object does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, format=None):
        request_hostdomain = request.query_params.get('host_domain', None)
        if not request_hostdomain:
            return Response({'detail':'Bad request, host_domain param is required'}, status=status.HTTP_400_BAD_REQUEST)
        instance = self._get_object(request_hostdomain)
        serializer = NormalUserTokenSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)