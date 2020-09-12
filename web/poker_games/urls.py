"""
Poll app URL Configuration

The `urlpatterns` list routes URLs to views which will be included in the main
urls file.
"""
from django.urls import path

from poker_games.views import (
    PokerGameCreateView, PokerGameListView, PokerGameDetailView,
    PokerGameDeleteView
)


urlpatterns = [ # pylint: disable=C0103
    path('poker-game/create', PokerGameCreateView.as_view(), name='poker-game-create'),
    path('poker-game/list', PokerGameListView.as_view(), name='poker-game-list'),
    path('poker-game/<int:pk>', PokerGameDetailView.as_view(), name='poker-game-detail'),
    path('poker-game/delete/<int:pk>', PokerGameDeleteView.as_view(), name='poker-game-delete'),
]
