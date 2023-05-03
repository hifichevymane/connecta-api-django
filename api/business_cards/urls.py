from django.urls import path
from . import views
# JWT auth views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # List of business cards and create them(GET and POST)
    path('business_cards/', views.BusinessCardsListCreateView.as_view()),
    # Get, update or delete business card by pk (POST, GET, UPDATE, DELETE, PUT, PATCH)
    path('business_cards/<int:pk>/', views.BusinessCardsRetrieveUpdateDestroyView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
