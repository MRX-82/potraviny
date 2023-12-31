from django.db import models


class Product(models.Model):
    """
    Model for saving products to the database.
    """
    name = models.CharField(max_length = 20)
    cost = models.IntegerField()
    articl = models.IntegerField()
    image = models.URLField(max_length=100, default='D')


class User(models.Model):
    """
    Model for saving users to the database.
    """
    name = models.CharField(max_length = 12)
    login = models.CharField(max_length = 16)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    cash = models.IntegerField(default = 0)
    status = models.IntegerField(default = 2)
    my_product = models.CharField(max_length = 20, default='none')

