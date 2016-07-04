from django.conf.urls import url

from . import views

app_name = 'teamBuilder'
urlpatterns = [
    url(r'^user/(?P<id>[0-9]+)', views.UserProfileView.as_view()),
    url(r'^team/(?P<id>[0-9]+)', views.TeamDetailView.as_view()),
    url(r'^project/create$', views.ProjectCreateView.as_view()),
    url(r'^project/createTeam/(?P<id>[0-9]+)', views.TeamCreateView.as_view()),
    url(r'^project/manage/(?P<id>[0-9]+)', views.ProjectManageView.as_view()), 
    url(r'^project/(?P<id>[0-9]+)', views.ProjectDetailView.as_view())
]
