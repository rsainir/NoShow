from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.

class ClientIntake(models.Model):
    PROGRESS_CHOICES_A = (
            ('1','Client Intake & Engagement Letter Sent'),
            ('2','Initial TM or Copyright Search'),
            ('3','Trademark Clearance Letter & Client Update'),
            ('4','Initial Filing'),
            ('5','USPTO Response Filing'),
            ('6','Publication for Opposition'),
            ('7','Filing Accepted and Completed with the USPTO')
        )
    PROGRESS_CHOICES_B = (
            ('1','Client Intake & Engagement Letter Sent'),
            ('2','Initial Draft Prepared'),
            ('3','Reviewed by Client'),
            ('4','Final Draft Sent')
        )
    PROGRESS_CHOICES_C = (
            ('1','Client Intake & Engagement Letter Sent'),
            ('2','Strategy and (or) Demand Letter Included'),
            ('3','Final Client Meeting')
        )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client_intake', null=True)
    firstName = models.CharField(u'First name',max_length=100, null=True)
    lastName = models.CharField(u'Last name', max_length=100, null=True)
    streetAddress = models.CharField(u'Street address', max_length=400, null=True)
    city = models.CharField(u'City', max_length=100, null=True)
    zipCode = models.IntegerField(u'Postal / Zip code', null=True)
    number = models.CharField(u'Phone number', max_length=12, null=True)
    employerName = models.CharField(u'Name of employer or business name if self-employed',max_length = 300, default='')
    advice = models.TextField(u'Briefly explain what you may need advice about or assistance with today', default='')
    partiesInvolved = models.TextField(u'Are there any other parties involved? (Examples: a friend, an employer, a neighbor, signor of a contract, etc. This should include parties on either side of your issue)', default='')
    desiredOutcome = models.TextField(u'Ideally, if things turn out precisely the way you want, what would be the outcome?', default='')
    acceptOutcome = models.TextField(u'Knowing that there are no guarantees, what final outcome can you reasonably accept?', default='')
    progress_A = models.CharField(max_length = 100, choices = PROGRESS_CHOICES_A, default = 1)
    progress_B = models.CharField(max_length = 100, choices = PROGRESS_CHOICES_B, default = 1)
    progress_C = models.CharField(max_length = 100, choices = PROGRESS_CHOICES_C, default = 1)

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
