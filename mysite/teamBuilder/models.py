from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    realname = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    school = models.CharField(max_length=20, blank=True)
    major = models.CharField(max_length=20, blank=True)
    grade = models.CharField(max_length=20, blank=True)
    # tags = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    description = models.TextField()
    role = models.CharField(max_length=20, choices=(('normal', 'normal'), ('special', 'special')), null=True)


class Project(models.Model):
    title = models.CharField(max_length=20, blank=True)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    description = models.TextField()
    # team_list = models.ManyToManyField('Team', related_name='team', blank=True)
    def __str__(self):
        return self.title


class Team(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='teamEnroll')
    name = models.CharField(max_length=20, blank=True)
    captain = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    members = models.ManyToManyField(User, related_name='teamJoin', blank=True)
    tags = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

