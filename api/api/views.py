from rest_framework import generics
from .serializers import CreateUserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


# User registration view
class UserRegistrationCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny, )
