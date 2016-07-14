from django.conf.urls import url

from . import views

app_name = 'teamBuilder'
urlpatterns = [
    url(r'^user/(?P<id>[0-9]+)', views.UserProfileView.as_view()),
    url(r'^team/(?P<id>[0-9]+)', views.TeamDetailView.as_view()),
    url(r'^project/create/$', views.ProjectCreateView.as_view()),
    url(r'^project/createTeam/(?P<id>[0-9]+)', views.TeamCreateView.as_view()),
    url(r'^project/manage/(?P<id>[0-9]+)', views.ProjectManageView.as_view()),
    url(r'^project/', views.ProjectDetailView.as_view()),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^user/activation/(?P<activation_key>\w+)/$', views.ActivationView),
    url(r'^$', views.IndexView.as_view(), name='index')
]
