from django.urls import path
from players import views

urlpatterns = [
    path('players/', views.PlayerList.as_view(), name="player-list"),
    path('player/<int:pk>/', views.PlayerDetail.as_view(), name='player-detail')
]