from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import User
from .models import Teams

# Register your models here.

class TeamsInline(admin.TabularInline):
    model = Teams
    can_delete = False
    verbose_name_plural = 'Teams'

class UserAdmin(BaseUserAdmin):
    inlines = (TeamsInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
