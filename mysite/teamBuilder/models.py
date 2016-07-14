from __future__ import unicode_literals
import django.utils.timezone as timezone
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db.models import signals
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.
class UserProfile(models.Model):
    owner          = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE, null=True)
    ROLE_CHOICE    = (('common', 'common'),
                      ('special', 'special'))
    realname       = models.CharField(max_length=100, blank=True, default='张三')
    phone          = models.CharField(max_length=100, blank=True, default='18800000000')
    school         = models.CharField(max_length=100, blank=True, default='Sun Yat-sen University')
    department     = models.CharField(max_length=100, blank=True, default='School of Data and Computer Science')
    major          = models.CharField(max_length=100, blank=True, default='Software Engineering')
    grade          = models.CharField(max_length=100, blank=True, default='2013')
    description    = models.TextField(blank=True, default="Enter your personal description here.")
    role           = models.CharField(max_length=20, choices=ROLE_CHOICE, blank=True, default='common')
    tags           = ArrayField(models.CharField(max_length=100), blank=True, default=['tag1', 'tag2', 'tag3'])
    activation_key = models.CharField(max_length=40, default="Not activated")

    def __str__(self):
        return (self.owner.username + "'s Profile")

def create_user_profile(sender, instance, created, **kwargs):
    """
    A hook function.
    When a user is created, its UserProfile will be created automatically.
    """
    if created:
        UserProfile.objects.create(owner=instance)

signals.post_save.connect(create_user_profile, sender=User)

@receiver(signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Project(models.Model):
    """
    The project's title is unique.
    """
    owner          = models.ForeignKey(UserProfile, related_name='project_published', on_delete=models.CASCADE, null=True)
    title          = models.CharField(max_length=100, blank=True, unique=True, default='Demo Project')
    description    = models.TextField(blank=True, default="Enter your description here")
    school         = ArrayField(models.CharField(max_length=200), blank=True, default=['Sun Yat-sen University', 'South China University of Technology'])
    department     = ArrayField(models.CharField(max_length=200), blank=True, default=['School of Data and Computer Science', 'School of Engineering'])
    major          = ArrayField(models.CharField(max_length=200), blank=True, default=['Software Engineering', 'Computer Science and Technology'])
    deadline       = models.DateTimeField('deadline', default=timezone.now, blank=True)
    min_num        = models.PositiveIntegerField(blank=True, default=3)
    max_num        = models.PositiveIntegerField(blank=True, default=10)

    def __str__(self):
        return self.title

class Team(models.Model):
    owner          = models.ForeignKey(UserProfile, related_name='team_captain', on_delete=models.CASCADE, null=True)
    project        = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team_enrolled')
    name           = models.CharField(max_length=100, blank=True, unique=True, default='Demo Team')
    tags           = ArrayField(models.CharField(max_length=100), blank=True, null=True, default=['tag1', 'tag2', 'tag3'])
    description    = models.TextField(default="Enter your description here")
    is_confirmed   = models.BooleanField(default=False)
    is_special     = models.BooleanField(default=False)
    member_list    = models.ManyToManyField(UserProfile, related_name='team_member', blank=True)
    candidate_list = models.ManyToManyField(UserProfile, related_name='team_candidate', blank=True)

    def __str__(self):
        return self.name

class Message(models.Model):
    """
    Define all kind of communication between users.
    Owner is receiver.
    """
    MSG_CHOICE = (
        ('COMMENT', 'Comment'),
        ('APPLY', 'Apply'),
    )
    owner     = models.ForeignKey(UserProfile, related_name='msg_received', on_delete=models.CASCADE, null=True)
    msg_type  = models.CharField(max_length=30, choices=MSG_CHOICE, default=(MSG_CHOICE[0]))
    content   = models.TextField(max_length=300, default="Enter your message here")
    post_time = models.DateTimeField('publish_time', default=timezone.now, null=True)
    sender    = models.ForeignKey(UserProfile, related_name='msg_sent', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.owner.realname + " " + self.msg_type + " " + self.content + " " + str(self.post_time))
