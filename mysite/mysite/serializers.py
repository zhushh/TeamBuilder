from rest_framework import serializers
from django.contrib.auth.models import User
from teamBuilder.models import *

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        # fields = '__all__'
        fields = ('url', 'owner', 'realname', 'phone', 'school', 'department', 'major', 'grade', 'description', 'role', 'tags', 'project_published', 'team_captain', 'team_member', 'team_candidate', 'comment_received', 'comment_made')
        read_only_fields = ('project_published', 'team_captain', 'comment_received', 'comment_made', 'team_member', 'team_candidate')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'user_profile')
        read_only_fields = ('username', 'user_profile',)
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if validated_data['email'] != '':
            instance.email = validated_data['email']
        if validated_data['password'] != '':
            instance.set_password(validated_data['password'])
        return instance

    def validate(self, data):
        email = data['email']
        password = data['password']
        users = User.objects.filter(email=data['email'])
        if len(users) != 0:
            instance = self.instance
            user = users[0]
            if instance != user:
                raise serializers.ValidationError("This email has been occupied")
        if len(password) < 8 or len(password) > 20:
            raise serializers.ValidationError("The password should be at least 8 characters and at most 20 characters")
        return data

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'title', 'owner', 'description', 'school', 'department', 'major', 'min_num', 'max_num', 'team_enrolled')
        read_only_fields = ('team_enrolled', 'owner')

    def validate(self, data):
        if data['min_num'] > data['max_num']:
            raise serializers.ValidationError("minimum number must be greater than maximum number ")
        return data

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'owner', 'project', 'name', 'tags', 'description', 'is_confirmed', 'is_special', 'member_list', 'candidate_list')
        read_only_fields = ('owner',)


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('owner',)


