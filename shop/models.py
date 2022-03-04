from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200,default="")
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
    image = models.CharField(max_length=500)