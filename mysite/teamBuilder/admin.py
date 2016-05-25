from django.contrib import admin
from .models import Profile, Team, Project
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    # verbose_name_plural = 'owners'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )
    list_display = ('id', 'username', 'email', 'is_staff', 'last_login')



@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'captain', 'project')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
