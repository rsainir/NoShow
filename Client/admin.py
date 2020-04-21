from django.contrib import admin
from .models import ClientIntake
from .models import Router
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

#admin.site.register(ClientIntake)
# Register your models here.

class ClientIntakeInline(admin.StackedInline):
    model = ClientIntake
    can_delete = False
    verbose_name_plural = 'Client Intake Form'
    fk_name = 'user'
    readonly_fields = ('firstName','lastName','streetAddress','city','zipCode','number','employerName','advice', 'partiesInvolved','desiredOutcome','acceptOutcome')
    

class Documents(admin.StackedInline):
    model=Router
    verbose_name_plural='Documents'
    fk_name='user'

class CustomUserAdmin(UserAdmin):
    inlines = (ClientIntakeInline, Documents,)
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request,obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

admin.site.site_header = 'Gonzalo Law Administration'
