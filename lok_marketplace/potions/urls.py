from django.urls import path
from . import views

urlpatterns = [
    path("", views.getPotions),
    path("", views.addPotion),
]
