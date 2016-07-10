from rest_framework import viewsets
from rest_framework import filters
from rest_framework.permissions import *
from mysite.serializers import *
from teamBuilder.models import *
from django.contrib.auth.models import User
from teamBuilder.permissions import *
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users' profile to be viewed or edited
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, )


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)
    permission_classes = [IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,
                          IsPublisherOrReadOnly,
                          ]

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.filter(owner=self.request.user)[0]
        serializer.save(owner=user_profile)

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teams to be viewed or edited
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.filter(owner=self.request.user)
        serializer.save(owner=user_profile[0], member_list=user_profile)

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.filter(owner=self.request.user)[0]
        serializer.save(owner=user_profile)
