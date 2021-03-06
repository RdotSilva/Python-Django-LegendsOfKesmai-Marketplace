from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from potions.models import Potion
from .serializers import PotionSerializer


class PotionsView(APIView):
    def get(self, request, format=None):
        potions = Potion.objects.all()
        serializer = PotionSerializer(potions, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PotionSerializer(data=request.data)  # Serialize data from request
        if serializer.is_valid():  # Check to ensure data is valid
            serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        id = request.data["id"]
        potion = Potion.objects.get(id=id)
        potion.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, *args, **kwargs):
        data = request.data

        # Fetch the potion using ID passed into request
        potion = Potion.objects.get(id=data["id"])

        # Update all potion data
        potion.category = data["category"]
        potion.itemId = data["itemId"]
        potion.image = data["image"]
        potion.name = data["name"]
        potion.slug = data["slug"]
        potion.save()

        serializer = PotionSerializer(potion)
        return Response(serializer.data)
