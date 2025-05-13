from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from listings.models import Listing
from reviews.models import Review
from datetime import date, timedelta

class ReviewCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username="reviewer", email="reviewer@example.com")
        self.listing = Listing.objects.create(
            user=self.user,
            title="Review Test Listing",
            description="A sample listing for testing reviews.",
            price=500.00,
            location="Sample Location",
            latitude=12.34,
            longitude=56.78,
            availability_start=date.today(),
            availability_end=date.today() + timedelta(days=30),
            room_type="Private",
            amenities=["Wi-Fi", "Heater"],
            property_images=["http://example.com/img.jpg"],
            is_pet_friendly=True
        )

        self.review_data = {
            "user": self.user,
            "listing": self.listing,
            "rating": 4,
            "comment": "Very good experience."
        }

    def test_create_review(self):
        self.review_data = {
            "user": self.user.user_id,
            "listing": self.listing.listing_id,
            "rating": 4,
            "comment": "Very good experience."
        }
        response = self.client.post("/reviews/", self.review_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_review_list(self):
        Review.objects.create(
            user=self.user,
            listing=self.listing,
            rating=5,
            comment="Excellent stay!"
        )
        response = self.client.get("/reviews/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_review(self):
        review = Review.objects.create(
            review_id="12345678-1234-5678-1234-567812345678",
            user=self.user,
            listing=self.listing,
            rating=3,
            comment="Initial comment"
        )
        updated_data = {
            "review_id": "12345678-1234-5678-1234-567812345678",
            "user": str(self.user.user_id),
            "listing": str(self.listing.listing_id),
            "rating": 5,
            "comment": "Updated comment"
        }
        response = self.client.put(reverse('review-detail', kwargs={'review_id': review.review_id}), updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["comment"], "Updated comment")

    def test_delete_review(self):
        review = Review.objects.create(
            review_id="12345678-1234-5678-1234-567812345678",
            user=self.user,
            listing=self.listing,
            rating=2,
            comment="Needs improvement"
        )
        response = self.client.delete(reverse('review-detail', kwargs={'review_id': review.review_id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
