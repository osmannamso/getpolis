from django.db import models


class Currency(models.Model):
    source_id = models.CharField(max_length=7)
    char_code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=255, unique=True)
    rate = models.FloatField()
