from rest_framework import serializers
from selling.models import Selling


class SellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selling
        fields = "__all__"
