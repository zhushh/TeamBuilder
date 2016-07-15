from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'owner', 'realname', 'phone', 'school', 'department', 'major', 'grade', 'description', 'role', 'tags', 'project_published', 'team_captain', 'team_member', 'team_candidate', 'msg_received', 'msg_sent')
        read_only_fields = ('project_published', 'team_captain', 'msg_received', 'msg_sent', 'team_member', 'team_candidate')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'user_profile')
        read_only_fields = ('user_profile',)
        # Sensitive password info will not be displayed but can be writen in.
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
        """
        Be aware of that partial update is not available in this method.
        Because auth.models.User's field has attr (required=True).
        """
        if validated_data['email'] != '':
            instance.email = validated_data['email']
        if validated_data['password'] != '':
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

    def validate_password(self, value):
        if len(value) < 8 or len(value) > 20:
            raise serializers.ValidationError("The password should be at least 8 characters and at most 20 characters")
        return value

    def validate_email(self, value):
        users = User.objects.filter(email=value)
        if len(users) != 0:
            # email has been registered
            user = users[0]
            if self.instance is None or self.instance != user:
                raise serializers.ValidationError("This email has been occupied")
        return value


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('url', 'title', 'owner', 'description', 'school', 'department', 'major', 'min_num', 'max_num', 'team_enrolled')
        read_only_fields = ('team_enrolled', 'owner')

    def validate(self, data):
        min_num = None
        max_num = None

        if self.instance is not None:
            min_num = self.instance.min_num
            max_num = self.instance.max_num
        if 'min_num' in data:
            min_num = data['min_num']
        if 'max_num' in data:
            max_num = data['max_num']

        if min_num > max_num:
            raise serializers.ValidationError("minimum number %s must be less than maximum number %s" % (min_num, max_num))
        return data

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ('url', 'owner', 'project', 'name', 'tags', 'description', 'is_confirmed', 'is_special', 'member_list', 'candidate_list')
        read_only_fields = ('owner',)

    def validate(self, data):
        """
        Supposing only members will be updated.
        Impose project restriction on members.
        Currently, school requirement and no one can participate two teams in the same project.
        """
        project_required_schools = None
        team_name = None
        if self.instance is None:
            project_required_schools = data['project'].school
            team_name = data['name']
        else:
            project_required_schools = self.initial_data.project.school
            team_name = self.initial_data.name

        if (self.instance is not None and self.instance.is_special == False) or (self.instance is None and data['is_special'] == False):

            if 'member_list' in data:
                for member in data['member_list']:
                    # required schools
                    if member.school not in project_required_schools:
                        raise serializers.ValidationError("%s from %s is not qualified to participate in this project. School requirement %s" % (member.realname, member.school, project_required_schools))
                    # join only one team in the same project
                    enrolled_team = Team.objects.filter(project=data['project'])
                    joined_team = enrolled_team.filter(member_list__owner__username=member.owner.username)
                    if (len(joined_team) >= 1 and joined_team[0].name != self.team_name) :
                        raise serializers.ValidationError("%s has already participated in this project." % member.realname)
        return data

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate_post_time(self, value):
        post_time = value
        current_time = timezone.now()
        if post_time > current_time:
            raise serializers.ValidationError("The post time is invalid")

    def validate(self, data):
        if data['owner'] == data['sender']:
            raise serializers.ValidationError("Receiver and Sender can't be the same guy.")
        return data
