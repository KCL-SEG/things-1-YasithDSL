from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Thing(models.Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(blank=True, max_length=120)
    quantity = models.SmallIntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0),
        ]
    )
