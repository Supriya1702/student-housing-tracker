from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import ListingSerializer
from uuid import uuid4
from datetime import datetime, timedelta

# Dummy data for listings
DUMMY_LISTINGS = [
    {
        "listing_id": str(uuid4()),
        "user": 1,  # References Alice
        "title": "Cozy Private Room Near Campus",
        "description": "A comfortable private room with WiFi and parking, perfect for students.",
        "price": 750.00,
        "location": "123 Main St, Amherst, MA 01002",
        "latitude": 42.3751,
        "longitude": -72.5199,
        "availability_start": "2025-06-01",
        "availability_end": "2026-05-31",
        "room_type": "Private",
        "amenities": ["WiFi", "Parking"],
        "is_pet_friendly": False,
        "property_images": ["https://example.com/images/room1.jpg"],
        "created_at": "2025-05-11T10:00:00Z",
        "updated_at": "2025-05-11T10:00:00Z"
    },
    {
        "listing_id": str(uuid4()),
        "user": 2,  # References Bob
        "title": "Spacious Entire Apartment",
        "description": "A fully furnished apartment with all amenities, ideal for a group of students.",
        "price": 1500.00,
        "location": "456 Elm St, Amherst, MA 01002",
        "latitude": 42.3800,
        "longitude": -72.5250,
        "availability_start": "2025-08-01",
        "availability_end": "2026-07-31",
        "room_type": "Entire",
        "amenities": ["WiFi", "Laundry", "Kitchen"],
        "is_pet_friendly": True,
        "property_images": ["https://example.com/images/apt1.jpg", "https://example.com/images/apt2.jpg"],
        "created_at": "2025-05-11T12:00:00Z",
        "updated_at": "2025-05-11T12:00:00Z"
    },
    {
        "listing_id": str(uuid4()),
        "user": 3,  # References Charlie
        "title": "Shared Room with Great Amenities",
        "description": "A shared room in a vibrant neighborhood, close to UMass campus.",
        "price": 500.00,
        "location": "789 Oak St, Amherst, MA 01002",
        "latitude": 42.3700,
        "longitude": -72.5100,
        "availability_start": "2025-07-01",
        "availability_end": "2026-06-30",
        "room_type": "Shared",
        "amenities": ["WiFi", "Gym", "Pool"],
        "is_pet_friendly": False,
        "property_images": ["https://example.com/images/room2.jpg"],
        "created_at": "2025-05-11T14:00:00Z",
        "updated_at": "2025-05-11T14:00:00Z"
    }
]

class ListingListCreateView(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        # Since we're using dummy data, we return the DUMMY_LISTINGS directly
        return DUMMY_LISTINGS

class ListingRetrieveView(generics.RetrieveAPIView):
    serializer_class = ListingSerializer
    lookup_field = 'listing_id'

    def get_queryset(self):
        # Since we're using dummy data, we return the DUMMY_LISTINGS directly
        return DUMMY_LISTINGS