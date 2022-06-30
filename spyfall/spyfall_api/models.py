from django.db import models

# Create your models here.
class Locations(models.Model):
    name = models.CharField(max_length=50, blank=False, default='')