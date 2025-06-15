from django.db import models
from django.contrib.auth.models import AbstractUser

"""
class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='userprofile', primary_key=True)
    profile_image = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.TextField(blank=True)
    contact_number = models.CharField(blank=True)

    def __str__(self):
        return f'{self.user.username} profile'
"""


class CustomUser(AbstractUser):
    profile_image = models.ImageField(
        upload_to='profile_images', blank=True, default='profile_images/default.png')
    bio = models.TextField(blank=True)
    contact_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username