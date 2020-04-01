from django.apps import AppConfig
<<<<<<< HEAD
from suit.apps import DjangoSuitConfig

class SuitConfig(DjangoSuitConfig):
	layout = 'horizontal'
=======

>>>>>>> 9d98b8f... commit

class ClientConfig(AppConfig):
    name = 'Client'

   # def ready(self):
    #    import Client.signals
