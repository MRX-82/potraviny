from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 12)
    login = models.CharField(max_length = 16)
    number = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length = 20)

