from django.db import models
from django.http import request
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Person(AbstractUser):
    #username
    #email
    professional = models.BooleanField(default=False)
    on_demand = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Appointment(models.Model):
    health_professional_username = models.CharField(max_length=50, null=True)
    user_username= models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True, null=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return "Appointment for " + self.first_name

    class Meta:
        ordering = ["-sent_date"]

class ChatRoom(models.Model):
    url = models.CharField(max_length=250, null=True)
