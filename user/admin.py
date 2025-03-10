from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ['is_activated']
        return []

admin.site.unregister(User)
admin.site.register(User, UserAdmin)