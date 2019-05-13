from rest_framework import serializers
from play.models import PlayGame


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = PlayGame
        fields = ('trump', 'player1', 'player2', 'player3', 'player4', 'deck')
