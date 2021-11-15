from django.db import models

# Create your models here.
class healthProfessional(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField()

class User(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    status = models.BooleanField()

class Appointment(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    professionalID =  models.ForeignKey(healthProfessional,on_delete=models.CASCADE)
    when = models.DateTimeField()

