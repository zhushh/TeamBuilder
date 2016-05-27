from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from api.serializers import *
from teamBuilder.models import *
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users' profile to be viewed or edited
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class RestrictionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows restrictions to be viewed or edited
    """
    queryset = Restriction.objects.all()
    serializer_class = RestrictionSerializer
