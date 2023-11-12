from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 12)
    login = models.CharField(max_length = 16)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length = 20)
    cash = models.IntegerField(default = 0)
    status = models.IntegerField(default = 2)

class Product(models.Model):
    user = models.ManyToManyField(User)
    name = models.CharField(max_length = 20)
    cost = models.IntegerField()
    articl = models.IntegerField()
    image = models.URLField(max_length=100, default='D')

