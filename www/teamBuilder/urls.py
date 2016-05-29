from django.conf.urls import url

from . import views

app_name = 'teamBuilder'
urlpatterns = [
    url(r'user_page/(?P<pk>[0-9]+)/$', views.UserPageView.as_view(), name='userpage'),
    url(r'team_page/(?P<pk>[0-9]+)/$', views.TeamPageView.as_view(), name='teampage'),
    url(r'project_page/(?P<pk>[0-9]+)/$', views.ProjectPageView.as_view(), name='projectpage'),

    url(r'project_create/$', views.ProjectCreateView.as_view(), name='project_create'),
    url(r'team_create/$', views.TeamCreateView.as_view(), name='team_create'),

    url(r'edit_user/$', views.UserEditView.as_view(), name='user_edit'),
    url(r'team_edit/(?P<pk>[0-9]+)/$', views.TeamEditView.as_view(), name='team_edit'),
    url(r'project_edit/(?P<pk>[0-9]+)/$', views.ProjectEditView.as_view(), name='project_edit'),

    url(r'team_delete/(?P<pk>[0-9]+)/$', views.TeamDeleteView.as_view(), name='team_delete'),
    url(r'project_delete/(?P<pk>[0-9]+)/$', views.ProjectDeleteView.as_view(), name='project_delete')
]
