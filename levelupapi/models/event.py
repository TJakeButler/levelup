from django.db import models


class Event(models.Model):

   
    event_time = models.DateTimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)