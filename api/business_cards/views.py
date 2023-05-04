from rest_framework import generics
from .models import BusinessCard
from .serializers import BusinessCardsSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Get all business cards and create one(GET, POST)
class BusinessCardsListCreateView(generics.ListCreateAPIView):
    # Which query set will execute in Django ORM
    queryset =  BusinessCard.objects.all()
    serializer_class = BusinessCardsSerializer
    permission_classes = (IsAuthenticated, )

    # Get only user's created business cards
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


# Retrieve business card, update and delete it(POST, PUT, PATCH, DELETE)
class BusinessCardsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BusinessCard.objects.all()
    serializer_class = BusinessCardsSerializer
    permission_classes = (IsAuthenticated, )
