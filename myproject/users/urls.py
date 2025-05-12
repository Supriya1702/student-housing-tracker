from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_users

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users', include(router.urls)),
    path('users-info/', get_users, name='get_users'),  # or whatever endpoint you want
]
