from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, get_users

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

urlpatterns = [
    path('users/', UserViewSet.as_view({'get': 'list', 'post': 'create'}), name='user-list'),
    path('users/<int:pk>/', UserViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='user-detail'),
]
