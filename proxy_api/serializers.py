from .models import KeyToken, HostDomain
from rest_framework import serializers

class KeyTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyToken
        fields = '__all__'
    