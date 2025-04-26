from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description=models.TextField()
    def __str__(self):
        return self.name

# class Participant(models.Model):
#     name=models.CharField(max_length=255)
#     email=models.EmailField(unique=True)
#     def __str__(self):
#         return self.name
    
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events_category' )
    participants = models.ManyToManyField(User, related_name='event_participant', blank=True)

    def __str__(self):
        return f"{self.name} - {self.date}" 
    

class RSVP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rsvps')
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='rsvps')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'event')

    def __str__(self):
        return f"{self.user.username} RSVP to {self.event.name}"


