from django.urls import path
from .views import ListingListCreateView, ListingRetrieveUpdateDestroyView

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listing-list-create'),
    path('listings/<uuid:listing_id>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail'),
]
