from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from Client.models import ClientIntake
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class CustomAuthForm(AuthenticationForm):
	username = forms.CharField(widget=TextInput(attrs={'class':'validate','placeholder': 'Username'}))
	password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
	def confirm_login_allowed(self, user):
		if not user.is_active:
			raise forms.ValidationError('There was a problem with your login.', code='invalid_login')

class ClientRegisterForm(UserCreationForm):
	required_css_class = 'required'
	first_name = forms.CharField(required = True,widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
	last_name = forms.CharField(required = True,widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
	email = forms.EmailField(required = True,max_length=200, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	username = forms.CharField(required = True,widget=forms.TextInput(attrs={'placeholder': 'Username'}))
	password1 = forms.CharField(label="Password",required = True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
	password2 = forms.CharField(label="Confirm Password",required = True, widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
	field_order = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2']


	class Meta:
		model = User
		fields = ['first_name','last_name','username', 'email', 'password1', 'password2']

	def clean_password2(self):
		first_name = self.cleaned_data.get('first_name')
		if not first_name:
			raise forms.ValidationError("You must input a first name")
		last_name = self.cleaned_data.get('last_name')
		if not last_name:
			raise forms.ValidationError("You must input a last name")
		username = self.cleaned_data.get('username')
		if not username:
			raise forms.ValidationError("You must input a username")
		email = self.cleaned_data.get('email')
		if not email:
			raise forms.ValidationError("You must input an email address")
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

class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
