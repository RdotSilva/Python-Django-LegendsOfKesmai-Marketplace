from django.urls import path
from .views import SellingView

urlpatterns = [
    path("", SellingView.as_view()),
]
