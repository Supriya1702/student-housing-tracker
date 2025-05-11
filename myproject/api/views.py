from rest_framework import generics
from .models import Listing
from .serializers import ListingSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.users import DUMMY_USERS

class ListingListCreateView(generics.ListCreateAPIView):
    queryset = Listing.objects.all() 
    serializer_class = ListingSerializer

class ListingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
