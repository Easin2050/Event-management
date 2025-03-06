from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description=models.TextField()

class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='events')
    participants = models.ManyToManyField("Participant",related_name='event_participant') 

class Participant(models.Model):
    name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    

