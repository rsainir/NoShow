from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from Client.models import clientIntake

class ClientRegisterForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')

<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 9d98b8f... commit
from Client.models import clientIntake

class ClientRegisterForm(UserCreationForm):
	email = forms.EmailField()
<<<<<<< HEAD
=======
>>>>>>> 6c159f3... Cleaned up directory, updated out of date imports. Added README.txt

=======
>>>>>>> ba88ad6... Heroku Deployment For Sprint 2
=======

>>>>>>> 9d98b8f... commit
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
class ClientIntakeForm(forms.ModelForm):

	class Meta:
		model = clientIntake
		fields = ['firstName','lastName','entry']
=======
#class ClientRegisterForm(UserCreationForm):
#	email = forms.EmailField(max_length=200, help_text='Required')

	

>>>>>>> 6c159f3... Cleaned up directory, updated out of date imports. Added README.txt
=======
class ClientIntakeForm(forms.ModelForm):
	class Meta:
		model = clientIntake
		fields = ['firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome','author']
>>>>>>> ba88ad6... Heroku Deployment For Sprint 2
=======
class ClientIntakeForm(forms.ModelForm):
	class Meta:
		model = clientIntake
		fields = ['firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome','author']
>>>>>>> 9d98b8f... commit
