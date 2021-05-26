from django.db import models

class Cricketer(models.Model):
    name = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    age = models.IntegerField()
    ipl_team = models.CharField(max_length=50)


