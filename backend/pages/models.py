from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='clubs')
    created_at = models.DateField()
    updated_at = models.DateField()
    logo = models.ImageField(upload_to='clubs')
    banner = models.ImageField(upload_to='clubs')
    event_manager = models.ForeignKey(User, on_delete=models.CASCADE)
    events = models.ManyToManyField('Event', related_name='clubs')

class Event(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey()
