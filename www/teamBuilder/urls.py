from django.conf.urls import url

from . import views

app_name = 'teamBuilder'
urlpatterns = [
    url(r'(?P<pk>[0-9]+)/user_page/$', views.UserPageView.as_view(), name='userpage'),
    url(r'(?P<pk>[0-9]+)/team_page/$', views.TeamPageView.as_view(), name='teampage'),
    url(r'(?P<pk>[0-9]+)/project_page/$', views.ProjectPageView.as_view(), name='projectpage'),

    url(r'project_create/$', views.ProjectCreateView.as_view(), name='project_create'),
    url(r'team_create/$', views.TeamCreateView.as_view(), name='team_create'),

    url(r'edit_user/$', views.UserEditView.as_view(), name='user_edit'),
    url(r'(?P<pk>[0-9]+)/team_edit/$', views.TeamEditView.as_view(), name='team_edit'),
    url(r'(?P<pk>[0-9]+)/project_edit/$', views.ProjectEditView.as_view(), name='project_edit'),

    url(r'(?P<pk>[0-9]+)/team_delete/$', views.TeamDeleteView.as_view(), name='team_delete'),
    url(r'(?P<pk>[0-9]+)/project_delete/$', views.ProjectDeleteView.as_view(), name='project_delete')
]
