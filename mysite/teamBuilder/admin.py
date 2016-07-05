from django.contrib import admin
from .models import Profile, Team, Project, Comment
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

class ProfileInline(admin.StackedInline):
    model        = Profile
    can_delete   = False

class UserAdmin(BaseUserAdmin):
    inlines      = (ProfileInline, )
    list_display = ('username', 'email', 'is_staff', 'last_login', 'profile')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', )

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'project')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'content', 'time', 'commentator')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
