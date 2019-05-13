from django import forms
from players.models import Player
from decks.models import Deck


class GameForm(forms.Form):
    bid = forms.IntegerField(max_value=100, label='Bid')
