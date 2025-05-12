from rest_framework.routers import DefaultRouter
from .views import SavedListingViewSet

router = DefaultRouter()
router.register('', SavedListingViewSet)
urlpatterns = router.urls