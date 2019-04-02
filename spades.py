import random
import itertools


class Card:     # card object has a rank and a suit
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def eq(self, rank, suit):   # check if cards are equal
        if self.rank == rank and self.suit == suit:
            return True
        else:
            return False

    def dispCard(self):  # display a card. will be edited
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
        print(('┌─────────┐\n'
               '│{}{}       │\n'
               '│         │\n'
               '│         │\n'
               '│    {}    │\n'
               '│         │\n'
               '│         │\n'
               '│       {}{}│\n'
               '└─────────┘\n\n').format(dispRank, fSpace, dispSuit, fSpace, dispRank))


class Player:   # player object. has a hand, score, bid, tricks, name, card on the table, and a turn
    def __init__(self, name, order):
        self.hand = []  # cards in hand
        self.score = 0  # total score for game
        self.bid = 0    # bid for hand
        self.tricks = 0 # tricks taken
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
        print("\n\nYour hand: ")
        self.sortHand()
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

    def playCard(self, trump):  # basically a stub to see if rest of game works.
        if trump > 0:           # will allow user to play a card and determine which card CPUs play
            self.cardOnTable = self.hand.pop(len(self.hand))
        else:
            self.cardOnTable = self.hand[0]
            self.hand.pop(0)
        self.cardOnTable.dispCard()


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
    trump = 0
    deal(4, deck, players)  # deal cards
    players[0].printHand()
    for p in players:
        if not p == players[0]:
            p.bet()
        else:
            p.bid = input('\n\nEnter your bid: ')
        print(p.name, ': ', p.bid)
    while len(players[0].hand) > 0:
        trick = players[0]
        players[0].printHand()
        print('Table: ')
        turn = 0
        while turn < 4:         # allow all players to play in order
            for player in players:
                if player.turnOrder == turn:
                    player.playCard(trump)
            turn += 1
        for player in players:          # determine who won trick
            if player.cardOnTable.rank > trick.cardOnTable.rank:
                trick.cardOnTable = player.cardOnTable
                trick = player
        trick.tricks += 1
        tempTurn = trick.turnOrder
        # not done yet!!! change who goes first
    for player in players:
        score(player)
        print(player.score, ' ', player.tricks, ' ', player.bid) # print scores at the end of hand


def score(player):      # how score is added up after each hand
    if (int(player.bid) < int(player.tricks) or int(player.bid) == int(player.tricks)) and (int(player.bid) > 0):
        player.score += int(player.bid) * 10
        player.score += int(player.tricks) - int(player.bid)
    elif int(player.bid) == 0:
        if player.tricks == 0:
            player.score += 100
        else:
            player.score -= 100
    else:
        player.score -= int(player.bid) * 10


options = 0     # menu stuff may be more options later
while options is not '9':
    if options == 0:
        intro = open("intro.txt", "r")
        for line in intro:
            print(line, end='', flush=True)
        options = input('\nEnter a number\nMenu:\n1: Play Spades\n2: View Rules\n9: Quit\n\n')
        intro.close()
    if options == '1':
        suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']       # seed for deck of cards
        ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        deck = build(suits, ranks)      # build deck and players
        player = Player('Human', 0)
        cpu1 = Player('CPU 1', 1)
        cpu2 = Player('CPU 2', 2)
        cpu3 = Player('CPU 3', 3)
        players = [player, cpu1, cpu2, cpu3]
        play(players, deck)
        options = '0'
    elif options == '2':                # everything else is more menu stuff for now
        rules = open("rules.txt", "r")
        for line in rules:
            print(line, end='', flush=True)
        options = '0'
        rules.close()
    elif options == '9':
        break
    else:
        options = input('\nEnter a number\nMenu:\n1: Play Spades\n2: View Rules\n9: Quit\n\n')
