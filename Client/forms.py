from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Client.models import ClientIntake

class ClientRegisterForm(UserCreationForm):
	required_css_class = 'required'
	email = forms.EmailField(required = True,max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	username = forms.CharField(required = True,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password1 = forms.CharField(label="Password",required = True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label="Confirm Password",required = True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))


	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

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

class ClientIntakeForm(forms.ModelForm):
	class Meta:
		model = ClientIntake
		fields = ['firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome']
