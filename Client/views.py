from django.contrib import messages
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import ClientRegisterForm
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from .forms import ClientIntakeForm
from .models import ClientIntake
from django.urls import reverse


#def client_file(request):
#	if request.method == 'GET':



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
			return redirect('client-intake-submit')
	else:
		form = ClientIntakeForm(instance=request.user.client_intake)

	return render(request, 'Client/client_intakeForm.html', {'form':form})

@login_required
def client_intake_submit(request):
	return render(request, 'Client/client_intake_submit.html',)

def client_page(request):
	return render(request, 'Client/client_home.html')

@login_required
def client_documents(request):
	return render(request, 'Client/client_documents.html')

def registration_page(request):
	if request.method == 'POST':
		form = ClientRegisterForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = False
			user.save()
			current_site = get_current_site(request)
			mail_subject = 'Activate your GL Law Client Account.'
			message = render_to_string('Client/acc_active_email.html', {
				'user': user,
				'domain': current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)),
				'token':account_activation_token.make_token(user),
				})
			to_email = form.cleaned_data.get('email')
			email = EmailMessage(
				mail_subject, message, to=[to_email]
			)
			email.send()
			return render(request,'Client/confirmation_requested.html')
	else:
		form = ClientRegisterForm(request.POST)
	return render(request, 'Client/client_registration.html', {'form': form})




@login_required
def client_profile_page(request):
	if request.method == 'GET':
		intake_forms = ClientIntake.objects.filter(user = request.user)

	return render(request, 'Client/client_profile_page.html', {'form_list':intake_forms, "choicesA": [x[1] for x in ClientIntake.PROGRESS_CHOICES_A],"choicesB": [x[1] for x in ClientIntake.PROGRESS_CHOICES_B],"choicesC": [x[1] for x in ClientIntake.PROGRESS_CHOICES_C]})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        #html = '<html> <body>Thank you for your email confirmation. Now you can login your account at the following link: <a class="nav-item nav-link" href={pathh}>Login</a></body></html>'
        # return redirect('home')
        return render(request, "Client/client_activated.html")
    else:
        return HttpResponse('Activation link is invalid!')
