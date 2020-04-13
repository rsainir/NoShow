from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from Client.models import clientIntake

class ClientRegisterForm(UserCreationForm):
	required_css_class = 'required'
	email = forms.EmailField(required = True,max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	username = forms.CharField(required = True,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password1 = forms.CharField(label="Password",required = True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label="Confirm Password",required = True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


<<<<<<< HEAD
<<<<<<< HEAD
=======

<<<<<<< HEAD
>>>>>>> 9d98b8f... commit
from Client.models import clientIntake
=======
from Client.models import ClientIntake
>>>>>>> 085f232... commit2

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
=======
	def clean_password2(self):
		username = self.cleaned_data.get('username')
		if not username:
			raise forms.ValidationError("You hellom your password")
		email = self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError("You must hellosword")
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')
		
		if not password2:
			raise forms.ValidationError("You must confirm your password")
		if password1 != password2:
			raise forms.ValidationError("Your passwords do not match")
		return password2

>>>>>>> c6447b9... trying to push from terminal
class ClientIntakeForm(forms.ModelForm):
	class Meta:
<<<<<<< HEAD
		model = clientIntake
		fields = ['firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome','author']
>>>>>>> 9d98b8f... commit
=======
		model = ClientIntake
		fields = ['firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome']
>>>>>>> 085f232... commit2
