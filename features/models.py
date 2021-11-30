from django.db import models
from django.http import request

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Appointment(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=50, null=True)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True, null=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ["-sent_date"]