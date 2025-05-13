from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from users.models import User
from verification.models import Verification

class VerificationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='verifier', email='verifier@example.com', password='testpass')
        self.verification_data = {
            "user": self.user.user_id,
            "document_type": "ID",
            "document_url": "http://example.com/doc.png",
            "status": "Pending"
        }

    def test_create_verification(self):
        response = self.client.post("/verifications/", self.verification_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["status"], "Pending")

    def test_list_verifications(self):
        Verification.objects.create(user=self.user, document_type="ID", document_url="http://example.com/id.png", status="Pending")
        response = self.client.get("/verifications/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_verification(self):
        verification = Verification.objects.create(user=self.user, document_type="Lease", document_url="http://example.com/lease.png", status="Approved")
        response = self.client.get(f"/verifications/{verification.verification_id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "Approved")

    def test_update_verification(self):
        verification = Verification.objects.create(user=self.user, document_type="Utility", document_url="http://example.com/bill.png", status="Pending")
        update_data = {
            "user": str(self.user.user_id),
            "document_type": "Utility",
            "document_url": "http://example.com/bill.png",
            "status": "Approved"
        }
        response = self.client.put(f"/verifications/{verification.verification_id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "Approved")

    def test_delete_verification(self):
        verification = Verification.objects.create(user=self.user, document_type="ID", document_url="http://example.com/id.png", status="Rejected")
        response = self.client.delete(f"/verifications/{verification.verification_id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
