from rest_framework import serializers
from .models import BusinessCard


# Serializer for Business card model
class BusinessCardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessCard
        # Which fields will be used for response
        exclude = ('owner', )

    # Owner id will automaticaly set for current user
    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        business_card = BusinessCard.objects.create(**validated_data)

        return business_card
