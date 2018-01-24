from django.urls import path
from .views import RankingsView


urlPatterns = [
    path("", RankingsView.as_view()),
]