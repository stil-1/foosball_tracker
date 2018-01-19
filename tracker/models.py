from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=256, null=False)
    created_date = models.DateTimeField(auto_now_add=True, null=False)
    modified_date = models.DateTimeField(auto_now=True, null=False)
    mu = models.FloatField()
    sigma = models.FloatField()
    wins = models.IntegerField()
    losses = models.IntegerField()


class Team(models.Model):
    players = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="team")
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


class Game(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_won')
    loser = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='games_lost')

