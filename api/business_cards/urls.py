from django.urls import path
from . import views

urlpatterns = [
    # List of business cards and create them(GET and POST)
    path('business_cards/', views.BusinessCardsListCreateView.as_view()),
    # Get, update or delete business card by pk (POST, GET, UPDATE, DELETE, PUT, PATCH)
    path('business_cards/<int:pk>/', views.BusinessCardsRetrieveUpdateDestroyView.as_view()),
]
