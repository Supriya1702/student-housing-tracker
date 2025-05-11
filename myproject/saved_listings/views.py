from rest_framework import viewsets
from .models import SavedListing
from .serializers import SavedListingSerializer

class SavedListingViewSet(viewsets.ModelViewSet):
    queryset = SavedListing.objects.all()
    serializer_class = SavedListingSerializer