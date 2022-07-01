from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from selling.models import Selling
from .serializers import SellingSerializer


class SellingView(APIView):
    def get(self, request, format=None):
        items_for_sale = Selling.objects.all()
        serializer = SellingSerializer(items_for_sale, many=True)
        return Response(serializer.data)
