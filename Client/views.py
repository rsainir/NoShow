from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientRegisterForm

from .forms import ClientIntakeForm
from .models import ClientIntake

@login_required
def client_intake_page(request):
	if request.method == 'POST':
		form = ClientIntakeForm(request.POST, instance=request.user.client_intake)
		
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('user')
			firstName = form.cleaned_data.get('firstName')
			lastName = form.cleaned_data.get('lastName')
			streetAddress = form.cleaned_data.get('streetAddress')
			city = form.cleaned_data.get('city')
			zipCode = form.cleaned_data.get('zipCode')
			number = form.cleaned_data.get('number')
			employerName = form.cleaned_data.get('employerName')
			advice = form.cleaned_data.get('advice')
			partiesInvolved = form.cleaned_data.get('partiesInvolved')
			desiredOutcome = form.cleaned_data.get('desiredOutcome')
			acceptOutcome = form.cleaned_data.get('acceptOutcome')
		
			messages.success(request, f'Client intake form completed')
			return redirect('client-page')
	else:
		form = ClientIntakeForm(instance=request.user.client_intake)

	return render(request, 'Client/client_intakeForm.html', {'form':form})


def client_page(request):
	return render(request, 'Client/client_home.html')

def registration_page(request):

	if request.method == 'POST':
		form = ClientRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Your Account Has Been Created, Please Log In')
			return redirect('login-page')
	else:
		form = ClientRegisterForm()

	return render(request, 'Client/client_registration.html', {'form':form})

@login_required
def client_profile_page(request):
	return render(request, 'Client/client_profile_page.html')
