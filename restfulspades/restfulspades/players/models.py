from django.db import models
from rspades import Player as p
import json


class Player(models.Model):
    hand = models.CharField(null=True, max_length=200)
    score = models.IntegerField(default=0)
    bid = models.IntegerField(default=0)
    tricks = models.IntegerField(default=0)
    name = models.CharField(null=True, max_length=30)
    cardOnTable = models.CharField(null=True, max_length=20)
    turnOrder = models.IntegerField(null=True)
    spotOnTable = models.IntegerField(null=True)
    isAI = models.BooleanField(default=True)

    def bet(self):  # betting. first part of each hand, may need corrections
        # Parse the JSON string that is the list of card objects into a regular list
        decodedList = json.loads(self.hand)

        # Unfortunately the strings in that list also need to be parsed from JSON to dicts of {suit:, rank:}.
        decodedHand = []
        for item in decodedList:
            decodedHand.append(json.loads(item))

        spades = 0
        hearts = 0
        clubs = 0
        diamonds = 0
        aces = 0
        kc, kd, kh, ks = 0, 0, 0, 0
        qc, qd, qh, qs = 0, 0, 0, 0
        asp = 0
        for card in decodedHand:
            if card['Suit'] == 'Spades':
                spades += 1
            if card['Suit'] == 'Clubs':
                clubs += 1
            if card['Suit'] == 'Hearts':
                hearts += 1
            if card['Suit'] == 'Diamonds':
                diamonds += 1
            if card['Suit'] == 'Clubs' and card['Rank'] == 13: #card.eq(13, 'Clubs'):
                kc = 1
            if card['Suit'] == 'Diamonds' and card['Rank'] == 13:
                kd = 1
            if card['Suit'] == 'Hearts' and card['Rank'] == 13:
                kh = 1
            if card['Suit'] == 'Spades' and card['Rank'] == 13:
                ks = 1
            if card['Suit'] == 'Clubs' and card['Rank'] == 12:
                qc = 1
            if card['Suit'] == 'Diamonds' and card['Rank'] == 12:
                qd = 1
            if card['Suit'] == 'Hearts' and card['Rank'] == 12:
                qh = 1
            if card['Suit'] == 'Spades' and card['Rank'] == 12:
                qs = 1
            if card['Suit'] == 'Spades' and card['Rank'] == 14:
                asp = 1
            if card['Rank'] == 14:
                aces += 1
        self.bid += aces
        if 5 > hearts > 2 and kh == 1:
            self.bid += 1
        if 5 > clubs > 2 and kc == 1:
            self.bid += 1
        if 5 > diamonds > 2 and kd == 1:
            self.bid += 1
        if 5 > spades > 2 and ks == 1:
            self.bid += 1
        if 5 > hearts > 3 and qh == 1:
            self.bid += 1
        if 5 > clubs > 3 and qc == 1:
            self.bid += 1
        if 5 > diamonds > 3 and qd == 1:
            self.bid += 1
        if spades > 3 and qs == 1:
            self.bid += 1
        if (hearts < 2 or clubs < 2 or diamonds < 2) and spades > 3:
            self.bid += (spades - asp - qs - ks - 2)
        elif (spades - ks - asp - qs) > 3:
            self.bid += (spades-ks-qs-asp-3)