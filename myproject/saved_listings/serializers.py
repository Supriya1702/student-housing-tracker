from rest_framework import serializers
from .models import SavedListing

class SavedListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedListing
        fields = '__all__'