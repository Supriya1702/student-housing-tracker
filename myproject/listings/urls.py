from django.urls import path
from .views import ListingListCreateView, ListingRetrieveView

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listings'),
    path('listings/<str:listing_id>/', ListingRetrieveView.as_view(), name='listing_detail'),
]