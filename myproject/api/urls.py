
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from listings.views import ListingListCreateView, ListingRetrieveUpdateDestroyView
# from reviews.views import ReviewViewSet
from saved_listings.views import SavedListingsListCreateView
from user_messages.views import UserMessageViewSet
from users.views import UserViewSet
from verification.views import VerificationViewSet
from users.views import get_users  # assuming get_users is a separate function

# router = DefaultRouter()
# router.register(r'reviews', ReviewViewSet, basename='review')
# router.register(r'saved-listings', SavedListingsListCreateView, basename='savedlisting')
# router.register(r'user-messages', UserMessageViewSet, basename='usermessage')
# router.register(r'users', UserViewSet, basename='user')
# router.register(r'verifications', VerificationViewSet, basename='verification')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('listings/', ListingListCreateView.as_view(), name='listings'),
#     path('listings/<uuid:pk>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail'),
#     path('users-info/', get_users, name='get_users'),  # to distinguish from DRF user list
# ]


