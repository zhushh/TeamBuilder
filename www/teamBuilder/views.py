from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from django.contrib.auth.models import User
from .models import *
from .forms import *

# Create your views here.

class UserPageView(generic.DetailView):
    model                = User
    template_name        = 'teamBuilder/user_page.html'

class TeamPageView(generic.DetailView):
    model                = Team
    template_name        = 'teamBuilder/team_page.html'

class ProjectPageView(generic.DetailView):
    model                = Project
    template_name        = 'teamBuilder/project_page.html'

class ProjectCreateView(generic.edit.CreateView):
    model                = Project
    template_name_suffix = '_form'
    fields = ['title', 'description']


class TeamCreateView(generic.edit.CreateView):
    model                = Team
    template_name_suffix = '_form'
    fields = ['project', 'name', 'tags', 'description', 'is_confirmed']


class ProjectEditView(generic.edit.UpdateView):
    model                = Project
    template_name_suffix = '_update_form'

class TeamEditView(generic.edit.UpdateView):
    model                = Team
    template_name_suffix = '_update_form'

class UserEditView(generic.edit.UpdateView):
    model                = User
    template_name_suffix = '_update_form'

class TeamDeleteView(generic.edit.DeleteView):
    model                = Team
    template_name_suffix = '_check_delete'
    success_rul = reverse_lazy('index')

class ProjectDeleteView(generic.edit.DeleteView):
    model                = Project
    template_name_suffix = '_check_delete'
    success_rul = reverse_lazy('index')
