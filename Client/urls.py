from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.client_page, name='client-page'),
	url(r'^register/$', views.registration_page, name='registration-page'),
	url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    	views.activate, name='activate'),
	path('', views.client_page, name='client-page'),
    #path('register/', views.registration_page, name='registration-page'),
	path('login/', auth_views.LoginView.as_view(template_name = 'Client/client_login.html'), name='login-page'),
	path('logout/', auth_views.LogoutView.as_view(template_name = 'Client/client_logout.html'), name='logout-page'),
	path('profile/', views.client_profile_page, name='client-profile-page'),
	path('intakeForm/', views.client_intake_page,name='client-intake-page'),

]
