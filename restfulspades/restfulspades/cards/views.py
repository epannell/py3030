from cards.models import Card
from cards.serializers import CardSerializer
from rest_framework import generics


class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer