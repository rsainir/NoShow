from django.apps import AppConfig
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
	layout = 'horizonta'

class ClientConfig(AppConfig):
    name = 'Client'
