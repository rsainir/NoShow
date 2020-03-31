from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clientIntake(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    streetAddress = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    zipCode = models.IntegerField()
    number = models.CharField(max_length=12)
    employerName = models.CharField(max_length = 300)
    advice = models.TextField()
    partiesInvolved = models.TextField()
    desiredOutcome = models.TextField()
    acceptOutcome = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    

