import random
import itertools
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']       # seed for deck of cards
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Card:     # card object has a rank and a suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def eq(self, rank, suit):   # check if cards are equal
        if self.rank == rank and self.suit == suit:
            return True
        else:
            return False

    def dispCard(self):  # display a card. for testing purposes only
        if self.rank == 14:
            dispRank = "A"
        elif self.rank == 11:
            dispRank = "J"
        elif self.rank == 12:
            dispRank = "Q"
        elif self.rank == 13:
            dispRank = "K"
        else:
            dispRank = self.rank
        dispSuits = ['♠', '♥', '♦', '♣']
        if self.suit == 'Spades':
            dispSuit = dispSuits[0]
        elif self.suit == 'Hearts':
            dispSuit = dispSuits[1]
        elif self.suit == 'Diamonds':
            dispSuit = dispSuits[2]
        elif self.suit == 'Clubs':
            dispSuit = dispSuits[3]
        if self.rank == 10:
            fSpace = ''
        else:
            fSpace = ' '
        print(dispRank, " of ", dispSuit)
        '''print(('┌─────────┐\n'
               '│{}{}       │\n'
               '│         │\n'
               '│         │\n'
               '│    {}    │\n'
               '│         │\n'
               '│         │\n'
               '│       {}{}│\n'
               '└─────────┘\n\n').format(dispRank, fSpace, dispSuit, fSpace, dispRank))'''


class Player:   # player object. has a hand, score, bid, tricks, name, card on the table, and a turn
    def __init__(self, name, order):
        self.hand = []  # cards in hand
        self.score = 0  # total score for game
        self.bid = 0    # bid for hand
        self.tricks = 0 # tricks taken
        self.bags = 0 # bags taken
        self.name = name    # player id
        self.cardOnTable = Card(0, 'none')  # blank card until another is played
        self.turnOrder = order  # order of play
        self.spotOnTable = order #place in table/original order of play

    def sortHand(self):     # make hand more readable
        for card in range(len(self.hand)):
            for card2 in range(len(self.hand)):
                if self.hand[card].suit < self.hand[card2].suit:
                    self.hand[card], self.hand[card2] = self.hand[card2], self.hand[card]
        for card in range(len(self.hand)):
            for card2 in range(len(self.hand)):
                if self.hand[card].rank < self.hand[card2].rank and self.hand[card].suit == self.hand[card2].suit:
                    self.hand[card], self.hand[card2] = self.hand[card2], self.hand[card]

    def printHand(self):    # print a hand so player can see
        print("\n\n", self.name, "hand: ")
        for card in self.hand:
            card.dispCard()

    def bet(self):  # betting. first part of each hand, may need corrections
        spades = 0
        hearts = 0
        clubs = 0
        diamonds = 0
        aces = 0
        kc, kd, kh, ks = 0, 0, 0, 0
        qc, qd, qh, qs = 0, 0, 0, 0
        asp = 0
        for card in self.hand:
            if card.suit == 'Spades':
                spades += 1
            if card.suit == 'Clubs':
                clubs += 1
            if card.suit == 'Hearts':
                hearts += 1
            if card.suit == 'Diamonds':
                diamonds += 1
            if card.eq(13, 'Clubs'):
                kc = 1
            if card.eq(13, 'Diamonds'):
                kd = 1
            if card.eq(13, 'Hearts'):
                kh = 1
            if card.eq(13, 'Spades'):
                ks = 1
            if card.eq(12, 'Clubs'):
                qc = 1
            if card.eq(12, 'Diamonds'):
                qd = 1
            if card.eq(12, 'Hearts'):
                qh = 1
            if card.eq(12, 'Spades'):
                qs = 1
            if card.eq(14, 'Spades'):
                asp = 1
            if card.rank == 14:
                aces += 1
        self.bid += aces
        if 5 > hearts > 1 and kh == 1:
            self.bid += 1
        if 5 > clubs > 1 and kc == 1:
            self.bid += 1
        if 5 > diamonds > 1 and kd == 1:
            self.bid += 1
        if spades > 2 and ks == 1:
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

    def score(self):  # how score is added up after each hand
        if (int(self.bid) < int(self.tricks) or int(self.bid) == int(self.tricks)) and (int(self.bid) > 0):
            self.score += int(self.bid) * 10
            self.score += int(self.tricks) - int(self.bid)
            self.bags += int(self.tricks) - int(self.bid)
        elif int(self.bid) == 0:
            self.bags += int(self.tricks) - int(self.bid)
            if self.tricks == 0:
                self.score += 100
            else:
                self.score -= 100
        else:
            self.score -= int(self.bid) * 10
        if self.bags >= 10:
            self.score -= 100
            self.bags -= 10

    def playCard(self, table):  # basically a stub to see if rest of game works.
        self.cardOnTable = self.hand[0]
        self.hand.pop(0)


'''
AI Pseudocode

 keep track of:
    played cards
    for given suit
    	if spade has been played
    		trump is broken
    	if >=8 cards played in suit or someone has played trump on that suit:
    		assume someone is out of that suit
    if trump is broken: 
    	can examine spades
    do you have high card in a suit: 
    	is anyone out of that suit:
    		look at next suit
    	else:
    		play high card
    else:
    	find suit with fewest cards:
    		do you have card >= 10?
    			play lowest of cards >= 10
    		else:
    			play low card
'''


class GameData:    # keeps track of game progress
    def __init__(self):
        self.cardsOnTable = [] # list of cards on the table
        self.playedCards = [] # list of cards that have been played
        self.playedSpades = 0 # how many cards have been played per suit
        self.playedHearts = 0
        self.playedDiamonds = 0
        self.playedClubs = 0
        self.heartsBroken = 0 # someone is likeley out of suit
        self.diamondsBroken = 0
        self.clubsBroken = 0
        self.trump = 0 # trump is broken

    def getCurrentState(self):
        for card in self.cardsOnTable:
            if card.suit == 'Spades':
                self.trump = 1
        for card in self.playedCards:
            if card.suit == 'Spades':
                self.playedSpades += 1
                self.trump = 1
            if card.suit == 'Hearts':
                self.playedHearts += 1
            if card.suit == 'Diamonds':
                self.playedDiamonds += 1
            if card.suit == 'Clubs':
                self.playedClubs += 1
            self.assumeTrump()

    def assumeTrump(self):
        if self.playedHearts >= 8:
            self.heartsBroken = 1
        if self.playedDiamonds >= 8:
            self.diamondsBroken = 1
        if self.playedClubs >= 8:
            self.clubsBroken = 1


def build(suits, ranks):    # build deck of cards
    temp = list(itertools.product(ranks, suits))
    deck = [Card(temp[i][0], temp[i][1]) for i in range(0, len(temp))]
    random.shuffle(deck)
    return deck


def deal(nPlayers, deck, players):  # deal cards
    j = 0
    while j < 52:
        for i in range(nPlayers):
            players[i].hand.append(deck[0])
            deck.pop(0)
            j += 1


def play(players, deck):  # overall function for playing the game, manages turns, scoring, and maybe other stuff that hasn't been reached yet
                          # played cards
    pass


deck = build(suits, ranks)      # build deck and players
player = Player('Human', 0)
cpu1 = Player('CPU 1', 1)
cpu2 = Player('CPU 2', 2)
cpu3 = Player('CPU 3', 3)
players = [player, cpu1, cpu2, cpu3]
deal(4, deck, players)
for p in players:
    p.sortHand()
    p.printHand()
    p.bet()
    print("\n", p.bid)
