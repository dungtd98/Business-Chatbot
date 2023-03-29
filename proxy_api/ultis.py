from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

def generate_key(text, salt, iterations):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=iterations,
    )
    key = kdf.derive(text.encode('utf-8'))
    key = base64.urlsafe_b64encode(key)
    cipher_suite = Fernet(key)
    return cipher_suite
# encrypted_data = cipher_suite.encrypt(b"This message is being encrypted and cannot be seen!")
# print(cipher_suite.decrypt(encrypted_data).decode())











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