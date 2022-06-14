from django.urls import path
from .views import PotionsView

urlpatterns = [
    path("", PotionsView.as_view()),
]
