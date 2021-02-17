from django.db import models


class Event(models.Model):

   
    event_time = models.DateTimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    location = models.CharField(max_length=255)
    scheduler = models.ForeignKey("Gamer", on_delete=models.CASCADE)

    @property
    def joined(self):
        return self.__joined

    @joined.setter
    def joined(self, value):
        self.__joined = value