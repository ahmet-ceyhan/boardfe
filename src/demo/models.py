from django.db import models


class Demo(models.Model):
    text = models.CharField(max_length=32, blank=False)
    number = models.IntegerField(blank=False)
