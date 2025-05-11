from django.db import models
import uuid
from django.core.exceptions import ValidationError
from users.models import User
from datetime import date

class Listing(models.Model):
    listing_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')

    title = models.CharField(max_length=255)
    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    availability_start = models.DateField()
    availability_end = models.DateField()

    room_type = models.CharField(
        max_length=20,
        choices=[
            ('Private', 'Private Room'),
            ('Shared', 'Shared Room'),
            ('Entire', 'Entire Apartment')
        ]
    )

    amenities = models.JSONField(default=list, blank=True, null=True)
    is_pet_friendly = models.BooleanField(default=False)
    property_images = models.JSONField(default=list, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        # Title validation
        if not self.title or len(self.title.strip()) < 5:
            raise ValidationError({'title': 'Title must be at least 5 characters long.'})

        # Description validation
        if not self.description or len(self.description.strip()) < 20:
            raise ValidationError({'description': 'Description must be at least 20 characters long.'})

        # Price validation
        if self.price <= 0:
            raise ValidationError({'price': 'Price must be a positive value.'})

        # Location validation
        if not self.location.strip():
            raise ValidationError({'location': 'Location is required.'})

        # Coordinate validation
        if not (-90 <= self.latitude <= 90):
            raise ValidationError({'latitude': 'Latitude must be between -90 and 90.'})
        if not (-180 <= self.longitude <= 180):
            raise ValidationError({'longitude': 'Longitude must be between -180 and 180.'})

        # Date validation
        if self.availability_end < self.availability_start:
            raise ValidationError({'availability_end': 'End date must be after start date.'})
        if self.availability_start < date.today():
            raise ValidationError({'availability_start': 'Start date cannot be in the past.'})

        # Room type check
        if self.room_type not in dict(self._meta.get_field('room_type').choices):
            raise ValidationError({'room_type': 'Invalid room type selected.'})

        # Images validation
        if not isinstance(self.property_images, list):
            raise ValidationError({'property_images': 'Property images must be a list of image URLs.'})

        # Amenities validation
        if not isinstance(self.amenities, list):
            raise ValidationError({'amenities': 'Amenities must be a list.'})

    def __str__(self):
        return f"{self.title} - {self.location}"
