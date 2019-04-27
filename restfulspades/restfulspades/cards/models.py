from django.db import models


class Card(models.Model):
    rank = models.IntegerField(unique=False, null=True)
    suit = models.CharField(max_length=20, unique=False, null=True)
