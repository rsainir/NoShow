from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class clientIntake(models.Model):

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
