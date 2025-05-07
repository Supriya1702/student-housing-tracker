from django.urls import path
from .views import ListingListCreateView, ListingRetrieveUpdateDestroyView, get_users

urlpatterns = [
    path('listings/', ListingListCreateView.as_view(), name='listings'),
    path('listings/<uuid:pk>/', ListingRetrieveUpdateDestroyView.as_view(), name='listing-detail'),
    path('users/', get_users, name='get_users'),
]
