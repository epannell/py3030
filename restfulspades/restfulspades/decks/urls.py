from django.urls import path
from decks import views

urlpatterns = [
    path('deck/', views.DeckList.as_view(), name="deck-list"),
]