from rest_framework.response import Response
from rest_framework.decorators import api_view
from potions.models import Potion
from .serializers import PotionSerializer


@api_view(["GET"])
def getPotions(request):
    potions = Potion.objects.all()
    serializer = PotionSerializer(potions, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def addPotion(request):
    serializer = PotionSerializer(data=request.data)  # Serialize data from request
    if serializer.is_valid():  # Check to ensure data is valid
        serializer.save()
    return Response(serializer.data)
