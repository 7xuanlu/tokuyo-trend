from django.db import models

class GoogleTrend(models.Model):
    location = models.CharField(max_length=30)
    time = models.DateTimeField()
    interest = models.IntegerField()
