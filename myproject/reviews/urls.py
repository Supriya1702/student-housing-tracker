from django.urls import path
from .views import ReviewListCreateView, ReviewRetrieveUpdateDestroyView

urlpatterns = [
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
    path('reviews/<uuid:review_id>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review-detail')
]