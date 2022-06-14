from rest_framework.response import Response
from rest_framework.views import APIView
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
