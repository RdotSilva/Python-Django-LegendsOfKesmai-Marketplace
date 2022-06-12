from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(["GET"])
def getPotions(request):
    potions = [
        {
            "name": "Strength Potion",
            "image": "item-00225.png",
            "slug": "strengthpotion",
            "itemId": "00225",
            "category": "potions",
        },
        {
            "name": "Dexterity Potion",
            "image": "item-00222.png",
            "slug": "dexteritypotion",
            "itemId": "00222",
            "category": "potions",
        },
    ]
    return Response(potions)
