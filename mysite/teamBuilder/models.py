from __future__ import unicode_literals

import django.utils.timezone as timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.


# user.teamAsCaptain
# user.teamAsMember
# user.projectPublished.all()
class Profile(models.Model):
    ROLE_CHOICE  = (('common', 'common'),
                   ('special', 'special'))

    owner        = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    realname     = models.CharField(max_length=40, blank=True, default='张三')
    phone        = models.CharField(max_length=40, blank=True, default='18800000000')
    school       = models.CharField(max_length=40, blank=True, default='Sun Yat-Sen University')
    department   = models.CharField(max_length=40, blank=True, default='School of Data and Computer Science')
    major        = models.CharField(max_length=40, blank=True, default='Software Engineering')
    grade        = models.CharField(max_length=40, blank=True, default='2013')
    description  = models.TextField(blank=True, default="This is a description")
    role         = models.CharField(max_length=20, choices=ROLE_CHOICE, blank=True, default='common')
    tags         = ArrayField(models.CharField(max_length=50), blank=True, default=['tag1', 'tag2', 'tag3'])
    commentList  = models.ManyToManyField('Comment', related_name='profileCommented')

    def __str__(self):
        return (self.owner.username + "'s Profile")


# project.teamEnroll.all()
class Project(models.Model):
    owner        = models.ForeignKey(User, related_name='project_published', on_delete=models.CASCADE, null=True)
    title        = models.CharField(max_length=20, blank=True, unique=True, default='Demo Project')
    description  = models.TextField(blank=True, default="Enter your description here")
    school       = ArrayField(models.CharField(max_length=50), blank=True, default=['Sun Yat-sen University', 'South China University of Technology'])
    department   = ArrayField(models.CharField(max_length=50), blank=True, default=['School of Data and Computer Science', 'School of Engineering'])
    major        = ArrayField(models.CharField(max_length=50), blank=True, default=['Software Engineering', 'Computer Science and Technology'])
    deadline     = models.DateTimeField('deadline', default=timezone.now, blank=True)
    min_num      = models.PositiveIntegerField(blank=True, default=3)
    max_num      = models.PositiveIntegerField(blank=True, default=10)

    def __str__(self):
        return self.title

class Team(models.Model):
    owner        = models.OneToOneField(User, related_name='teamAsCaptain', on_delete=models.CASCADE, null=True)
    project      = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, related_name='teamEnroll')
    name         = models.CharField(max_length=20, blank=True, unique=True, default='Demo Team')
    tags         = ArrayField(models.CharField(max_length=50), blank=True, default=['tag1', 'tag2', 'tag3'])
    description  = models.TextField(default="Enter your description here")
    memberList   = models.ManyToManyField(User, related_name='teamAsMember')
    is_confirmed = models.BooleanField(default=False)
    is_special   = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# comment.profileCommented.all()
class Comment(models.Model):
    owner        = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content      = models.CharField(max_length=50, default="Enter your comment here")
    time         = models.DateTimeField('publish_time', default=timezone.now, null=True)

    def __str__(self):
        return (self.owner.username + " " + self.content + " " + str(self.time))


