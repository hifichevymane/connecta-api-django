from rest_framework import serializers
from django.contrib.auth.models import User


# User registration serializer
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        # Password will not displayed in JSOM response
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            email=validated_data['email']
        )

        # Set hashed password in User model
        user.set_password(validated_data['password'])
        user.save()

        return user
