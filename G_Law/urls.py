"""G_Law URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/client/admin', admin.site.urls),
    path('client/profile/client/admin', admin.site.urls),
    path('client/documents/client/admin', admin.site.urls),
    path('client/intakeForm/client/admin', admin.site.urls),
    path('client/', include('Client.urls')),
    url(r'client/^$', views.test_redirect4, name='test_redirect4'),
    url(r'^$', views.test_redirect1, name='test_redirect1'),
    url(r'^$', views.test_redirect2, name='test_redirect2'),
    url(r'^client/profile/admin/$', views.test_redirect3, name='test_redirect3'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
