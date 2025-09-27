from django.db import models

# Create your models here.
class Game(models.Model):
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    winner = models.CharField(max_length=100)
    date_played = models.DateTimeField(auto_now_add=True)
