from django.db import models
from players.models import Player
from decks.models import Deck


class PlayGame(models.Model):
    trump = models.IntegerField(null=True)
    player1 = models.ForeignKey(Player, related_name='player1', on_delete=models.PROTECT)
    player2 = models.ForeignKey(Player, related_name='player2', on_delete=models.PROTECT)
    player3 = models.ForeignKey(Player, related_name='player3', on_delete=models.PROTECT)
    player4 = models.ForeignKey(Player, related_name='player4', on_delete=models.PROTECT)
    deck = models.ForeignKey(Deck, related_name='deck', on_delete=models.PROTECT)


    #
    # def deal(self):  # deal cards
    #     nPlayers = 4
    #     j = 0
    #     while j < 52:
    #         for i in range(nPlayers):
    #             self."player + {0}".format(i).hand.append(self.deck[0])
    #             self.deck.pop(0)
    #             j += 1
    #
    # def score(Player):  # how score is added up after each hand
    #     if (int(Player.bid) < int(Player.tricks) or int(Player.bid) == int(Player.tricks)) and (int(Player.bid) > 0):
    #         Player.score += int(Player.bid) * 10
    #         Player.score += int(Player.tricks) - int(Player.bid)
    #     elif int(Player.bid) == 0:
    #         if Player.tricks == 0:
    #             Player.score += 100
    #         else:
    #             Player.score -= 100
    #     else:
    #         Player.score -= int(Player.bid) * 10
    #
    # def play(self):  # overall function for playing the game
    #     self.trump = 0
    #     self.deal()  # deal cards
    #     self.players[0].printHand()
    #     for p in self.players:
    #         if not p == self.players[0]:
    #             p.bet()
    #         else:
    #             p.bid = input('\n\nEnter your bid: ')
    #         print(p.name, ': ', p.bid)
    #     while len(self.players[0].hand) > 0:
    #         trick = self.players[0]
    #         self.players[0].printHand()
    #         print('Table: ')
    #         turn = 0
    #         while turn < 4:  # allow all players to play in order
    #             for player in self.players:
    #                 if player.turnOrder == turn:
    #                     player.playCard(self.trump)
    #             turn += 1
    #         for player in self.players:  # determine who won trick
    #             if player.cardOnTable.rank > trick.cardOnTable.rank:
    #                 trick.cardOnTable = player.cardOnTable
    #                 trick = player
    #         trick.tricks += 1
    #         tempTurn = trick.turnOrder
    #         # not done yet!!! change who goes first
    #     for player in self.players:
    #         self.score(player)
    #         print(player.score, ' ', player.tricks, ' ', player.bid)  # print scores at the end of hand

