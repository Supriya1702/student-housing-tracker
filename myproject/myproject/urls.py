"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse

from listings.views import ListingListCreateView, ListingRetrieveUpdateDestroyView
from reviews.views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView
from saved_listings.views import SavedListingsListCreateView, SavedListingRetrieveUpdateDestroyView
from user_messages.views import UserMessageViewSet
from users.views import UserViewSet
from verification.views import VerificationViewSet
from users.views import get_users
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


def root_view(request):
    return JsonResponse({"message": "Welcome to the Student Housing Tracker API"})

urlpatterns = [
    path('', root_view),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # Include API routes

]

# listings/urls.py (app-level)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('listings/', ListingListCreateView.as_view(), name='listings'),# urls.py
    path('listings/<uuid:listing_id>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail'),

    path('users-info/', get_users, name='get_users'),

    path('reviews/', ReviewListCreateView.as_view(), name='reviews'),
    path('reviews/<uuid:review_id>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail'),

    path('saved_listings/', SavedListingsListCreateView.as_view(), name='listing-list-create'),
    path('saved_listings/<uuid:saved_id>/', SavedListingRetrieveUpdateDestroyView.as_view(), name='saved-listing-detail'),

    path('user-messages/', UserMessageViewSet.as_view({'get': 'list', 'post': 'create'}), name='usermessage-list'),
    path('user-messages/<int:pk>/', UserMessageViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='usermessage-detail'),

    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),

    path('verifications/', VerificationViewSet.as_view({'get': 'list', 'post': 'create'}), name='verification-list'),
    path('verifications/<uuid:pk>/', VerificationViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='verification-detail'),
]
