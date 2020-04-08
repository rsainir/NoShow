from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Client.models import ClientIntake

class ClientRegisterForm(UserCreationForm):
	email = forms.EmailField(max_length=200, help_text='Required')

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ClientIntakeForm(forms.ModelForm):
	class Meta:
		model = ClientIntake
		fields = ['firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome']
