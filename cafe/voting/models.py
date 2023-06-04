from django.db import models

class Dessert(models.Model):
    name = models.CharField(max_length=100)
    votes = models.PositiveIntegerField(default=0)