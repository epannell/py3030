from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from players.models import Player
from .forms import GameForm


def playGame(request):

    players = Player.objects.all()

    if request.method == 'POST':
        form = GameForm(request.POST)

        if form.is_valid():

            for player in players:
                if player.isAI:
                    player.bet()
                else:
                    player.bid = form.cleaned_data['bid']
                player.save()
            return HttpResponseRedirect('/play/')

    else:
        form = GameForm()

    return render(request, 'play.html', {'form': form, 'players': players})

