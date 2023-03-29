from django.shortcuts import render
from rest_framework.views import APIView
from .ultis import generate_key
import os
from dotenv import load_dotenv
load_dotenv('.env')
from rest_framework.response import Response
import json
import base64
import requests
# Create your views here.
text = os.environ['SECRECT_KEY']
salt = bytes(os.environ['SALT_STRING'].encode('utf-8'))
openai_api_key = os.environ['OPENAI_API_KEY']
iterations = 100000
cipher = generate_key(text, salt, iterations)

# class ProxyAPIView(APIView):
#     proxy_host = "https://api.openai.com/"
#     # source = None
#     def get_proxyhost(self):
#         return self.proxy_host
#     def get_request_url(self, request):
#         host = self.get_proxyhost()
#         path = request.get_full_path()
#         if path:
#             return ''.join([host, path])
#     def get_query_params(self, request):
#         if request.query_params:
#             return request.query_params.copy()
#         return {}
#     def get_request_data(self, request):
#         if 'application/json' in request.content_type:
#             return json.dumps(request.data)
#         return request.data
#     def get_request_files(self, request):
#         files = {}
#         if request.FILES:
#             for field, content in request.FILES.items():
#                 files[field] = content
#         return files
        
#     def get_headers(self, request):
        
#         authorization_header = request.headers.get('Authorization', None)
#         if authorization_header:
#             request.META['HTTP_AUTHORIZATION'] = "Bearer "+cipher.decrypt(authorization_header).decode()       
#         return request.headers
    
#     def proxy(self, request, *args, **kwargs):
#         url = self.get_request_url(request)
#         params = self.get_query_params(request)
#         data = self.get_request_data(request)
#         headers = self.get_headers(request)
#         response = requests.request(
#             request.method, url,
#             params = params,
#             data = data,
#             headers=headers,
#         )
#         return Response(response)
    
#     def get(self, request, *args, **kwargs):
#         return self.proxy(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.proxy(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.proxy(request, *args, **kwargs)

#     def patch(self, request, *args, **kwargs):
#         return self.proxy(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.proxy(request, *args, **kwargs)

class ProxyAPIView(APIView):
    proxy_host = "https://api.openai.com"
    def post(self, request, format=None):
        authorization_header = request.headers.get('Authorization', None)
        auth_key = "Bearer "+cipher.decrypt(authorization_header).decode()
        # request.META['HTTP_AUTHORIZATION']=("Bearer "+cipher.decrypt(authorization_header).decode())

        url = self.proxy_host+request.get_full_path()
        
        headers = {'Authorization':auth_key}
        
        data = request.data
        response = requests.post(
            url=url,
            headers=headers,
            json=data,
        )
        return Response(response.json())

class GetEncryptToken(APIView):
    def get(self, request):
        encrypt_token = cipher.encrypt(openai_api_key.encode())
        return Response({"token":encrypt_token})