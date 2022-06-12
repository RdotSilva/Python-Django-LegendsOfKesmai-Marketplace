from django.db import models


class Potion(models.Model):
    category = models.CharField(max_length=200)
    itemId = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.name
