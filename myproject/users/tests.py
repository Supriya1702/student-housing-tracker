from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

class UserModelTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="test@example.com",
            password="securepassword123",
            first_name="Test",
            last_name="User",
            phone_number="1234567890",
            role="Student",
            is_verified=True,
            profile_picture="http://example.com/profile.jpg"
        )

    def test_user_creation(self):
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(self.user.email, "test@example.com")
        self.assertTrue(self.user.check_password("securepassword123"))
        self.assertEqual(self.user.role, "Student")

    def test_user_str_method(self):
        self.assertEqual(str(self.user), "Test User (test@example.com)")

class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="adminuser",
            email="admin@example.com",
            password="adminpass",
            role="Admin",
            is_verified=True
        )
        self.url = reverse("user-list")  # Make sure your router uses basename='user'

    def test_list_users(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)

    def test_create_user(self):
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password": "newpassword",
            "role": "Student"
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(email="new@example.com").exists())

class DummyUsersTestCase(APITestCase):
    def test_get_dummy_users(self):
        url = reverse("get_users")  # Ensure your URLconf names it "get_users"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
