from .models import KeyToken
from rest_framework import serializers

class KeyTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = KeyToken
        fields = '__all__'