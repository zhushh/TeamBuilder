from rest_framework import serializers
from django.contrib.auth.models import User
from teamBuilder.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'user', 'realname', 'phone', 'school', 'department', 'major', 'grade', 'description', 'role', 'tags', 'commentList')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'title', 'publisher', 'description')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'project', 'name', 'captain', 'memberList', 'tags', 'description', 'is_confirmed')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'marker', 'content', 'time')

class RestrictionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restriction
        fields = ('url', 'school', 'department', 'major', 'min_num', 'max_num')
