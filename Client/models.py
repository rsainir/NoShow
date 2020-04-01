from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clientIntake(models.Model):
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
>>>>>>> ba88ad6... Heroku Deployment For Sprint 2
