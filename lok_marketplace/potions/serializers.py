from rest_framework import serializers
from potions.models import Potion


class PotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Potion
        fields = "__all__"
