from django.contrib import admin
from .models import ClientIntake
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#admin.site.register(ClientIntake)
# Register your models here.

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