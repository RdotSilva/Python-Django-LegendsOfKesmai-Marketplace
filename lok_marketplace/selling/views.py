from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from selling.models import Selling
from .serializers import SellingSerializer


class SellingView(APIView):
    #TODO: Add get request for all items for sale
