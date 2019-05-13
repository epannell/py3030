from rest_framework import serializers
from players.models import Player


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('hand', 'score', 'bid', 'tricks', 'name', 'cardOnTable', 'turnOrder', 'spotOnTable', 'isAI')