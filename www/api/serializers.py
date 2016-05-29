from rest_framework import serializers
from django.contrib.auth.models import User
from teamBuilder.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    project_published = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'profile', 'project_published')

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'user', 'realname', 'phone', 'school', 'department', 'major', 'grade', 'description', 'role', 'tags', 'commentList')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        fields = ('url', 'title', 'owner', 'description', 'school', 'department', 'major', 'min_num', 'max_num')

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'project', 'name', 'owner', 'memberList', 'tags', 'description', 'is_confirmed')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('url', 'owner', 'content', 'time')


