from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
4
# Create your models here.

ROLE_CHOICE = (('common', 'common'), ('special', 'special'))

# user.teamAsCaptain
# user.teamAsMember
# user.projectPublished.all()
class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    realname    = models.CharField(max_length=20, blank=True)
    phone       = models.CharField(max_length=20, blank=True)
    school      = models.CharField(max_length=20, blank=True)
    department  = models.CharField(max_length=20, blank=True)
    major       = models.CharField(max_length=20, blank=True)
    grade       = models.CharField(max_length=20, blank=True)
    description = models.TextField(default="This is a description")
    role        = models.CharField(max_length=20, choices=ROLE_CHOICE, null=True,
                                   default=('common', 'common'))
    tags        = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    commentList = models.ManyToManyField('Comment', related_name='profileCommented',
                                         blank=True)

    def __str__(self):
        return (self.user.username + "'s Profile")


# project.teamEnroll.all()
class Project(models.Model):
    title       = models.CharField(max_length=20, blank=True)
    publisher   = models.ForeignKey(User, related_name='projectPublished',
                                    on_delete=models.CASCADE, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.title


class Team(models.Model):
    project      = models.ForeignKey(Project, on_delete=models.CASCADE, null=True,
                                     related_name='teamEnroll')
    name         = models.CharField(max_length=20, blank=True)
    captain      = models.OneToOneField(User, related_name='teamAsCaptain',
                                        on_delete=models.CASCADE, blank=True, null=True)
    memberList   = models.ManyToManyField(User, related_name='teamAsMember', blank=True)
    tags         = ArrayField(models.CharField(max_length=20), blank=True, null=True)
    description  = models.TextField(default="This is a description")
    is_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return self.name


# comment.profileCommented.all()
class Comment(models.Model):
    marker  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(max_length = 50, default="This is a comment")
    time    = models.DateTimeField()

    def __str__(self):
        return self.marker.username + " " + self.content + " " + str(self.time)


class Restriction(models.Model):
    school     = models.CharField(max_length=20, blank=True)
    department = models.CharField(max_length=20, blank=True)
    major      = models.CharField(max_length=20, blank=True)
    min_num    = models.PositiveIntegerField(null=True, blank=True)
    max_num    = models.PositiveIntegerField(null=True, blank=True)
