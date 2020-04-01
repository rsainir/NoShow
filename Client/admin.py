from django.contrib import admin
<<<<<<< HEAD
from .models import clientIntake
<<<<<<< HEAD
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
=======
=======
from .models import ClientIntake
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
>>>>>>> 085f232... commit2

#admin.site.register(ClientIntake)
# Register your models here.
<<<<<<< HEAD
>>>>>>> 9d98b8f... commit
=======

class ClientIntakeInline(admin.StackedInline):
    model = ClientIntake
    can_delete = False
    verbose_name_plural = 'Client Intake Form'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ClientIntakeInline, )
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
>>>>>>> 085f232... commit2
