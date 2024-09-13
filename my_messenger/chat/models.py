from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Model for chat rooms
class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

# Model for messages in a room
class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username}: {self.content[:50]}'

    class Meta:
        ordering = ['timestamp']
