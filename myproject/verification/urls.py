from rest_framework.routers import DefaultRouter
from .views import VerificationViewSet

router = DefaultRouter()
router.register('', VerificationViewSet)
urlpatterns = router.urls