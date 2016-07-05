from rest_framework import serializers
from django.contrib.auth.models import User
from teamBuilder.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    #project_published = serializers.PrimaryKeyRelatedField(many=True, queryset=Project.objects.all())
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'profile', 'project_published', 'team_candidate', 'team_member', 'comment_made')
        # fields = '__all__'

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        #fields = '__all__'
        fields = ('url', 'owner', 'realname', 'phone', 'school', 'department', 'major', 'grade', 'description', 'role', 'tags', 'comment_received')

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Project
        #fields = '__all__'
        fields = ('url', 'title', 'owner', 'description', 'school', 'department', 'major', 'min_num', 'max_num', 'team_enrolled')

    def validate(self, data):
        if data['min_num'] > data['max_num']:
            raise serializers.ValidationError("minimum number must be greater than maximum number ")
        return data

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        # fields = ('url', 'project', 'name', 'owner', 'memberList', 'tags', 'description', 'is_confirmed')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('url', 'owner', 'content', 'time')

