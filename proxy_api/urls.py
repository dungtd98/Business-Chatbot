from django.urls import re_path, path, include

from .views import ProxyAPIView, EncryptTokenListView, GetEncryptToken
urlpatterns = [
    path('api/', ProxyAPIView.as_view(), name='proxy_api'),
    path('token/', EncryptTokenListView.as_view(), name='admin_encrypt_token'),
    path('token/user-access-token/',GetEncryptToken.as_view(), name='user_encrypt_token')
]
