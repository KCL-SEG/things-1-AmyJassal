from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Thing (models.Model):
    name = models.CharField(max_length=20, unique = True)
    description = models.CharField(max_length=40, blank = True)
    quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])