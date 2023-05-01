from rest_framework import serializers
from .models import BusinessCard


# Serializer for Business card model
class BusinessCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCard
        # Which fields will be used for response
        fields = '__all__'
