from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from players.models import Player
from decks.models import Deck
from .forms import GameForm


def playGame(request):

    # Get player objects from database
    players = Player.objects.all()

    # Get deck object from database. Calls .all() but there should only be the one we pre-made.
    deck = Deck.objects.all()[0]

    # If it was a POST we need to make a new form
    if request.method == 'POST':
        form = GameForm(request.POST)

        # If form was valid after creation
        if form.is_valid():

            # Loop through players to initialize bids
            for player in players:
                if player.isAI:
                    player.bet()
                else:
                    player.bid = form.cleaned_data['bid']

            # deal to players
            deck.deal(players)
            deck.save()
            for p in players:
                p.save()

            return HttpResponseRedirect('/play/')

    # If it wasn't a POST just return the old one
    else:
        form = GameForm()

    # Render the form
    return render(request, 'play.html', {'form': form, 'players': players})

