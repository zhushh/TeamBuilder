from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.

class UserProfileView(TemplateView):
	template_name = 'accounts/profile.html'

class TeamDetailView(TemplateView):
	template_name = 'team/team_detail.html'

class ProjectCreateView(TemplateView):
	template_name = 'project/create_project.html'

class TeamCreateView(TemplateView):
	template_name = 'team/create_team.html'

class ProjectManageView(TemplateView):
	template_name = 'project/manage_project.html'

class ProjectDetailView(TemplateView):
	template_name = 'project/project_detail.html'