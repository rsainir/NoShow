from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientRegisterForm

from .forms import ClientIntakeForm
from .models import clientIntake

@login_required
def client_intake_page(request):
	if request.method == 'POST':
		form = ClientIntakeForm(request.POST)
		if form.is_valid():
			fs = form.save(commit = False)
			fs.username = request.user
			firstName = form.cleaned_data.get('firstName')
			lastName = form.cleaned_data.get('lastName')
			entry = form.cleaned_data.get('entry')
			fs.save()
		
			messages.success(request, f'Client intake form completed')
			return redirect('client-profile-page')
	else:
		form = ClientIntakeForm()
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

	return render(request, 'Client/client_registration.html', {'form': form})


@login_required
def client_profile_page(request):
	if request.method == 'GET':
		intake_forms = clientIntake.objects.filter(username = request.user)

	return render(request, 'Client/client_profile_page.html', {'form_list':intake_forms, "choices": [x[1] for x in clientIntake.PROGRESS_CHOICES]})
