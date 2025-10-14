from rest_framework import serializers
from .models import Service

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # We include all fields from the model
        fields = ['id', 'title', 'slug', 'summary', 'detailed_description', 'image']