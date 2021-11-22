from django.db import models

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name + " " + self.last_name

# class Appointment(models.Model):
#     userID = models.ForeignKey(User, on_delete=models.CASCADE)
#     professionalID =  models.ForeignKey(User,on_delete=models.CASCADE)
#     when = models.DateTimeField()

