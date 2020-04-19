from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

<<<<<<< HEAD
class clientIntake(models.Model):
<<<<<<< HEAD
<<<<<<< HEAD

    PROGRESS_CHOICES = (
            ('1','Submitted'),
            ('2','Recevied'),
            ('3','Filed'),
            ('4','Resolved')
        )
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    entry = models.TextField(max_length = 100, default = 'ENTRY_DATA')
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)

    progress = models.CharField(max_length = 100, choices = PROGRESS_CHOICES, default = 1)

    def __str__(self):
      return f'{self.firstName}, {self.lastName}, {self.entry}, {self.progress}'


      class Meta:
        ordering = ['date_created']
=======
=======
>>>>>>> 9d98b8f... commit
=======
class ClientIntake(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_intake')
>>>>>>> 085f232... commit2
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
<<<<<<< HEAD
    author = models.ForeignKey(User, on_delete=models.CASCADE)
<<<<<<< HEAD
>>>>>>> ba88ad6... Heroku Deployment For Sprint 2
=======
=======
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_intake', null=True)
    firstName = models.CharField(u'First name',max_length=100)
    lastName = models.CharField(u'Last name', max_length=100)
    streetAddress = models.CharField(u'Street address', max_length=400)
    city = models.CharField(u'City', max_length=100)
    zipCode = models.IntegerField(u'Postal / Zip code')
    number = models.CharField(u'Phone number', max_length=12)
    employerName = models.CharField(u'Name of employer or business name if self-employed',max_length = 300, default='')
    advice = models.TextField(u'Briefly explain what you may need advice about or assistance with today', default='')
    partiesInvolved = models.TextField(u'Are there any other parties involved? (Examples: a friend, an employer, a neighbor, signor of a contract, etc. This should include parties on either side of your issue)', default='')
    desiredOutcome = models.TextField(u'Ideally, if things turn out precisely the way you want, what would be the outcome?', default='')
    acceptOutcome = models.TextField(u'Knowing that there are no guarantees, what final outcome can you reasonably accept?', default='')

>>>>>>> cfe5fd2... sarah_intake / raul_register&forgot / rohan_login
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
<<<<<<< HEAD


>>>>>>> 085f232... commit2


    

>>>>>>> 9d98b8f... commit
=======
>>>>>>> cfe5fd2... sarah_intake / raul_register&forgot / rohan_login
