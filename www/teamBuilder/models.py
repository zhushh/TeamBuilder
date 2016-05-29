from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

# Create your models here.



# user.teamAsCaptain
# user.teamAsMember
# user.projectPublished.all()
class Profile(models.Model):
    ROLE_CHOICE = (('common', 'common'),
                   ('special', 'special'))

    user        = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    realname    = models.CharField(max_length=20, blank=True, default='张三')
    phone       = models.CharField(max_length=20, blank=True, default='18800000000')
    school      = models.CharField(max_length=20, blank=True, default='Sun Yat-Sen University')
    department  = models.CharField(max_length=20, blank=True, default='School of Data and Computer Science')
    major       = models.CharField(max_length=20, blank=True, default='Software Engineering')
    grade       = models.CharField(max_length=20, blank=True, default='2013')
    description = models.TextField(default="This is a description")
    role        = models.CharField(max_length=20, choices=ROLE_CHOICE, null=True,
                                   default=('common', 'common'))
    tags        = ArrayField(models.CharField(max_length=20), blank=True, null=True, default=['tag1', 'tag2', 'tag3'])
    commentList = models.ManyToManyField('Comment', related_name='profileCommented',
                                         blank=True)

    def __str__(self):
        return (self.user.username + "'s Profile")


# project.teamEnroll.all()
class Project(models.Model):
    title       = models.CharField(max_length=20, blank=True)
    publisher   = models.ForeignKey(User, related_name='projectPublished',
                                    on_delete=models.CASCADE, blank=True)
    description = models.TextField(default="This is a description")


    def __str__(self):
        return self.title


class Team(models.Model):
    project      = models.ForeignKey(Project, on_delete=models.CASCADE, null=True,
                                     related_name='teamEnroll')
    name         = models.CharField(max_length=20, blank=True)
    captain      = models.OneToOneField(User, related_name='teamAsCaptain',
                                        on_delete=models.CASCADE, blank=True, null=True)
    memberList   = models.ManyToManyField(User, related_name='teamAsMember', blank=True)
    tags         = ArrayField(models.CharField(max_length=20), blank=True, null=True, default=['tag1', 'tag2', 'tag3'])
    description  = models.TextField(default="This is a description")
    is_confirmed = models.BooleanField(default=False)


    def __str__(self):
        return self.name


# comment.profileCommented.all()
class Comment(models.Model):
    marker  = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.CharField(max_length = 50, default="This is a comment")
    time    = models.DateTimeField('publish_time')

    def __str__(self):
        return self.marker.username + " " + self.content + " " + str(self.time)


class Restriction(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE, blank=True, null=True)
    school     = models.CharField(max_length=40, blank=True, default='Sun Yat-Sen University')
    department = models.CharField(max_length=40, blank=True, default='School of Data and Computer Science')
    major      = models.CharField(max_length=40, blank=True, default='Software Engineering')
    min_num    = models.PositiveIntegerField(null=True, blank=True, default=3)
    max_num    = models.PositiveIntegerField(null=True, blank=True, default=10)
