from django.db import models


# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=25)
    year = models.DateField(blank=True, null=True)
