from rest_framework import viewsets
from .models import Verification
from .serializers import VerificationSerializer

class VerificationViewSet(viewsets.ModelViewSet):
    queryset = Verification.objects.all()
    serializer_class = VerificationSerializer