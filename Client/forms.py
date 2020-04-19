from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Client.models import clientIntake

class ClientRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class ClientIntakeForm(forms.ModelForm):
	
	class Meta:
		model = clientIntake
		fields = ['firstName','lastName','entry']