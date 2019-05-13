from django.urls import path
from play import views

urlpatterns = [
    path('play/', views.playGame),
]
