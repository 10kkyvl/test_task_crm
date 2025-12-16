from django.urls import path
from .views import ClientListAPIView, DealListAPIView


urlpatterns = [
    path("clients/", ClientListAPIView.as_view()),
    path("deals/", DealListAPIView.as_view()),
]
