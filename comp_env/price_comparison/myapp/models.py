from django.db import models

# Create your models here.
class amfp(models.Model):
    aprod = models.CharField(max_length=100)
    aprice = models.CharField(max_length=100)
    fprod = models.CharField(max_length=100)
    fprice = models.CharField(max_length=100)