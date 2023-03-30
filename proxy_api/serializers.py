from .models import KeyToken, HostDomain
from rest_framework import serializers

class AdminKeyTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyToken
        fields = '__all__'

class NormalUserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyToken
        fields = ('id','hostdomain','access_token')