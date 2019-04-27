from decks.models import Deck
from decks.serializers import DeckSerializer
from rest_framework import generics


class DeckList(generics.ListCreateAPIView):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
