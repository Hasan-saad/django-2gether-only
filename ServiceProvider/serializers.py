from .models import ServicProvider
from rest_framework import serializers

class ServiceProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServicProvider
        fields = '__all__'









