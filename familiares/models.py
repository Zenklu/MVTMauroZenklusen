from django.db import models
from datetime import datetime

class Relative(models.Model):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    ocupation = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    born= models.DateField(max_length=50)
    active = models.BooleanField(default=True)
    date = models.DateField(default = datetime.today)
