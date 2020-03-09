from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ClientRegisterForm

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
	return render(request, 'Client/client_profile_page.html')
