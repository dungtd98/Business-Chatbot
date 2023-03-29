from django.urls import re_path, path, include

from .views import ProxyAPIView, GetEncryptToken
urlpatterns = [
    path('api/', ProxyAPIView.as_view(), name='proxy_api'),
    path('token/', GetEncryptToken.as_view(), name='get_encrypt_token')
]
