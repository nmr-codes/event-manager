from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='clubs')
    created_at = models.DateField()
    
class Event(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    created_at = models.DateField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='events')
    updated_at = models.DateField()
