from django.db import models

# Create your models here.
class Thing(models.Model):
    username = models.CharField(unique=True)
    description = models.CharField()
    quantity = models.IntegerField()
