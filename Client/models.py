from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

#def user_directory_path(instance,filename):
   # return '{0}/{1}'.format(instance.user.username,filename)

# Create your models here.
#class Router(models.Model):
 #   user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_files', null=True)
  #  specifications=models.FileField(upload_to=user_directory_path)
  
   # def __User__(self):
    #    return self.user

class ClientIntake(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_intake', null=True)
    firstName = models.CharField(u'First name',max_length=100,default='')
    lastName = models.CharField(u'Last name', max_length=100, default='')
    streetAddress = models.CharField(u'Street address', max_length=400, default='')
    city = models.CharField(u'City', max_length=100, default='')
    zipCode = models.IntegerField(u'Postal / Zip code', default=0)
    number = models.CharField(u'Phone number', max_length=12, default='')
    employerName = models.CharField(u'Name of employer or business name if self-employed',max_length = 300, default='')
    advice = models.TextField(u'Briefly explain what you may need advice about or assistance with today', default='')
    partiesInvolved = models.TextField(u'Are there any other parties involved? (Examples: a friend, an employer, a neighbor, signor of a contract, etc. This should include parties on either side of your issue)', default='')
    desiredOutcome = models.TextField(u'Ideally, if things turn out precisely the way you want, what would be the outcome?', default='')
    acceptOutcome = models.TextField(u'Knowing that there are no guarantees, what final outcome can you reasonably accept?', default='')

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

#@receiver(post_save, sender=User)
#def create_user_router(sender, instance, created, **kwargs):
 #   if not created:
  #      Router.objects.create(user=instance)
   # instance.router.save()
   




    

