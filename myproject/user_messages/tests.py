from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from listings.models import Listing
from user_messages.models import Message
from datetime import date, timedelta

class MessageCRUDTestCase(APITestCase):
    def setUp(self):
        self.sender = User.objects.create(username="sender", email="sender@example.com")
        self.receiver = User.objects.create(username="receiver", email="receiver@example.com")
        self.listing = Listing.objects.create(
            user=self.sender,
            title="Sample Listing",
            description="A place to stay.",
            price=1000.00,
            location="Amherst",
            latitude=42.37,
            longitude=-72.52,
            availability_start=date.today(),
            availability_end=date.today() + timedelta(days=30),
            room_type="Private",
            amenities=["Wi-Fi"],
            property_images=["http://example.com/img.jpg"],
            is_pet_friendly=True
        )
        self.message_data = {
            "sender": self.sender.user_id,
            "receiver": self.receiver.user_id,
            "listing": self.listing.listing_id,
            "content": "Is this property still available?"
        }

    def test_create_message(self):
        response = self.client.post("/user-messages/", self.message_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("message_id", response.data)

    def test_get_messages(self):
        Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            listing=self.listing,
            content="Test message"
        )
        response = self.client.get("/user-messages/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_update_message(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            listing=self.listing,
            content="Initial message"
        )
        updated_data = {
            "sender": self.sender.user_id,
            "receiver": self.receiver.user_id,
            "listing": self.listing.listing_id,
            "content": "Updated message"
        }
        response = self.client.put(f"/user-messages/{message.message_id}/", updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["content"], "Updated message")

    def test_delete_message(self):
        message = Message.objects.create(
            sender=self.sender,
            receiver=self.receiver,
            listing=self.listing,
            content="To be deleted"
        )
        response = self.client.delete(f"/user-messages/{message.message_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)