from rest_framework.response import Response
from rest_framework.decorators import api_view
from potions.models import Potion
from .serializers import PotionSerializer


@api_view(["GET"])
def getPotions(request):
    potions = Potion.objects.all()
    serializer = PotionSerializer(potions, many=True)
    return Response(serializer.data)
