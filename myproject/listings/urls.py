# listings/urls.py
from rest_framework.routers import DefaultRouter
from .views import ListingViewSet

router = DefaultRouter()
router.register(r'', ListingViewSet)  # '' means base URL will be /api/listings/

urlpatterns = router.urls
