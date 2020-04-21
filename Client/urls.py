from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from . import views
from .forms import CustomAuthForm

urlpatterns = [
	url(r'^signin/', auth_views.LoginView.as_view(template_name = 'Client/client_login.html', authentication_form=CustomAuthForm), name='signin'),
	url(r'^$', views.client_profile_page, name='client-profile-page'),
	url(r'^register/$', views.registration_page, name='registration-page'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    	views.activate, name='activate'),
	path('logout/', auth_views.LogoutView.as_view(template_name = 'Client/client_logout.html'), name='logout-page'),
	url(r'^profile/$', views.client_profile_page, name='client-profile-page'),
	path('intakeForm/', views.client_intake_page,name='client-intake-page'),
	path('intakeForm/confirm',views.client_intake_submit,name='client-intake-submit'),
    path('documents/',views.client_documents, name='client-documents'),
	path('^password_reset/', auth_views.PasswordResetView.as_view(template_name='Client/password_reset_form.html'), name='password_reset'),
    path('^password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Client/password_reset_done.html'), name='password_reset_done'),
	url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.PasswordResetConfirmView.as_view(template_name="Client/password_reset_confirm.html"), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name='Client/password_reset_complete.html'), name='password_reset_complete'),

]
