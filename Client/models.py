from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class ClientIntake(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_intake')
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
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    def __User__(self):
        return self.user

@receiver(post_save, sender=User)
def create_or_update_user_client_intake(sender, instance, created, **kwargs):
    try:
        instance.client_intake.save()
    except ObjectDoesNotExist:
        ClientIntake.objects.create(user=instance)
   # if not created:
    #    ClientIntake.objects.create(user=instance)
    #instance.client_intake.save()




    

