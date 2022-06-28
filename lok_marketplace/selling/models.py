from django.db import models

# Create your models here.
class Selling(models.Model):
    category = models.CharField(max_length=200)
    itemId = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    price = models.IntegerField(max_length=9)
    quantity = models.IntegerField(max_length=3)

    def __str__(self):
        return self.name
