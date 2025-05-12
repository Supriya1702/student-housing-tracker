from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from listings.models import Listing
from saved_listings.models import SavedListing
from datetime import date, timedelta

class SavedListingCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="tester", email="tester@example.com")
        self.listing = Listing.objects.create(
            user=self.user,
            title="Test Listing",
            description="Nice student room.",
            price=800.00,
            location="UMass Amherst",
            latitude=42.39,
            longitude=-72.53,
            availability_start=date.today(),
            availability_end=date.today() + timedelta(days=30),
            room_type="Private",
            amenities=["Desk", "Wi-Fi"],
            property_images=["http://example.com/photo.jpg"],
            is_pet_friendly=False
        )
        self.saved_listing_data = {
            "user": str(self.user.user_id),
            "listing": str(self.listing.listing_id)
        }

    def test_create_saved_listing(self):
        response = self.client.post("/saved_listings/", self.saved_listing_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("saved_id", response.data)

    def test_get_saved_listings(self):
        SavedListing.objects.create(user=self.user, listing=self.listing)
        response = self.client.get("/saved_listings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_delete_saved_listing(self):
        saved = SavedListing.objects.create(user=self.user, listing=self.listing, saved_id="12345678-1234-5678-1234-567812345678")
        response = self.client.delete(reverse('saved-listing-detail', kwargs={'saved_id': str(saved.saved_id)}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
