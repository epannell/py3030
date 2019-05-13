from django.db import models


class Card(models.Model):
    rank = models.IntegerField(unique=False, null=True)
    suit = models.CharField(max_length=20, unique=False, null=True)


    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
