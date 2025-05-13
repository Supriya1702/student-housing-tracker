from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from listings.models import Listing
from datetime import date, timedelta

class ListingCRUDTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', email='test@example.com')

        self.listing_data = {
            "user": str(self.user.user_id),  # Pass user ID as string
            "title": "Test Room",
            "description": "A very nice place to stay for students.",
            "price": 750.00,
            "location": "UMass Amherst",
            "latitude": 42.386,
            "longitude": -72.529,
            "availability_start": str(date.today()),
            "availability_end": str(date.today() + timedelta(days=30)),
            "room_type": "Private",
            "amenities": ["Wi-Fi", "Heater"],
            "property_images": ["http://example.com/image1.jpg"],
            "is_pet_friendly": False
        }

    def test_create_listing(self):
        response = self.client.post(reverse('listings'), self.listing_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_listing_list(self):
        Listing.objects.create(
            user=self.user,
            title="Test Room",
            description="A very nice place to stay for students.",
            price=750.00,
            location="UMass Amherst",
            latitude=42.386,
            longitude=-72.529,
            availability_start=date.today(),
            availability_end=date.today() + timedelta(days=30),
            room_type="Private",
            amenities=["Wi-Fi", "Heater"],
            property_images=["http://example.com/image1.jpg"],
            is_pet_friendly=False
        )
        response = self.client.get(reverse('listings'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_listing(self):
        listing = Listing.objects.create(
            listing_id="12345678-1234-5678-1234-567812345678",
            user=self.user,
            title="Test Room",
            description="A very nice place to stay for students.",
            price=750.00,
            location="UMass Amherst",
            latitude=42.386,
            longitude=-72.529,
            availability_start=date.today(),
            availability_end=date.today() + timedelta(days=30),
            room_type="Private",
            amenities=["Wi-Fi", "Heater"],
            property_images=["http://example.com/image1.jpg"],
            is_pet_friendly=False
        )
        updated_data = self.listing_data.copy()
        updated_data['title'] = 'Updated Room'
        updated_data['user'] = str(self.user.user_id)  # Must include user
        response = self.client.put(reverse('listing-detail', kwargs={'listing_id': listing.listing_id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Updated Room')

    def test_delete_listing(self):
        listing = Listing.objects.create(
            listing_id="12345678-1234-5678-1234-567812345678",
            user=self.user,
            title="Test Room",
            description="A very nice place to stay for students.",
            price=750.00,
            location="UMass Amherst",
            latitude=42.386,
            longitude=-72.529,
            availability_start=date.today(),
            availability_end=date.today() + timedelta(days=30),
            room_type="Private",
            amenities=["Wi-Fi", "Heater"],
            property_images=["http://example.com/image1.jpg"],
            is_pet_friendly=False
        )
        response = self.client.delete(reverse('listing-detail', kwargs={'listing_id': listing.listing_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
