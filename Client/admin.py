from django.contrib import admin
from .models import clientIntake
<<<<<<< HEAD

=======
>>>>>>> ba88ad6... Heroku Deployment For Sprint 2

admin.site.register(clientIntake)
# Register your models here.

class ClientIntakeModelAdmin(admin.ModelAdmin):

	def name(obj):
		return obj.firstName + " " + obj.lastName

	list_display = (name, 'entry', 'progress')

	readonly_fields = (name, 'entry', 'date_created')

	fields = (name, 'entry','progress', 'date_created')

admin.site.register(clientIntake, ClientIntakeModelAdmin)
