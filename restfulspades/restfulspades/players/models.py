from django.db import models


class Player(models.Model):
    hand = models.CharField(null=True, max_length=200)
    score = models.IntegerField(null=True)
    bid = models.IntegerField(null=True)
    tricks = models.IntegerField(null=True)
    name = models.CharField(null=True, max_length=30)
    cardOnTable = models.CharField(null=True, max_length=20)
    turnOrder = models.IntegerField(null=True)
    spotOnTable = models.IntegerField(null=True)


