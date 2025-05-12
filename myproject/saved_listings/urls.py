from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import SavedListingsListCreateView, SavedListingRetrieveUpdateDestroyView

urlpatterns = [
    path('saved_listings/', SavedListingsListCreateView.as_view(), name='saved-listing-list-create'),
    path('saved_listings/<uuid:saved_id>/', SavedListingRetrieveUpdateDestroyView.as_view(), name='saved-listing-detail')
]