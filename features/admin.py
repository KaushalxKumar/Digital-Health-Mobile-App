from django.contrib import admin
from features.models import *
from features.forms import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = Person
    add_form = CreateUserForm

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User Role',
            {
                'fields': (
                    'professional',
                    'on_demand',
                )
            }
        )
    )

admin.site.register(Person, CustomUserAdmin)
admin.site.register(Appointment)
admin.site.register(ChatRoom)