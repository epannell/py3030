from django.db import models
from cards.models import Card
import json
import itertools
import random


class Deck(models.Model):
    cards = models.CharField(max_length=1000)

    def build(self):  # build deck of cards
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']  # seed for deck of cards
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        temp = list(itertools.product(ranks, suits))
        deck = [Card(temp[i][0], temp[i][1]) for i in range(0, len(temp))]
        random.shuffle(deck)
        cardList = []

        for card in deck:
            cardList.append({str(card.suit), int(card.rank)})

        self.cards = json.dumps(cardList)
