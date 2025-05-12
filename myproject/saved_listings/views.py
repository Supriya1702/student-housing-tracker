from rest_framework import generics
from .models import SavedListing
from .serializers import SavedListingSerializer

class SavedListingsListCreateView(generics.ListCreateAPIView):
    queryset = SavedListing.objects.all()
    serializer_class = SavedListingSerializer

class SavedListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SavedListing.objects.all()
    serializer_class = SavedListingSerializer
    lookup_field = 'saved_id'
