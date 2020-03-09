from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_page, name='client-page'),
    path('register/', views.registration_page, name='registration-page'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Client/client_login.html'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Client/client_logout.html'), name='logout-page'),
    path('profile/', views.client_profile_page, name='client-profile-page'),

]
