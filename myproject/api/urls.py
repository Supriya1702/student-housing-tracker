from django.urls import path
from .views import ListingListCreateView, ListingRetrieveUpdateDestroyView, get_users, get_listings

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listing-list-create'),
    path('listings/<uuid:pk>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-retrieve-update-destroy'),
    path('users/', get_users, name='get-users'),
    path('listings/dummy/', get_listings, name='get-dummy-listings'),
]