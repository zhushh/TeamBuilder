from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from .models import *
from .forms import *
import hashlib
import random
import re

# Create your views here.

class UserProfileView(TemplateView):
	template_name = 'teamBuilder/accounts/profile.html'

class TeamDetailView(TemplateView):
	template_name = 'teamBuilder/team/team_detail.html'

class ProjectCreateView(TemplateView):
	template_name = 'teamBuilder/project/create_project.html'

class TeamCreateView(TemplateView):
	template_name = 'teamBuilder/team/create_team.html'

class ProjectManageView(TemplateView):
	template_name = 'teamBuilder/project/manage_project.html'

class ProjectDetailView(TemplateView):
	template_name = 'teamBuilder/project/project_detail.html'


class RegisterView(FormView):
    template_name = 'teamBuilder/accounts/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('teamBuilder:index')

    def mail_validate(username, to_email):
        subject = u'Teambuilder用户验证'
        from_email = 'teambuilder@sina.com'
        
        # generate activation code
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        username = username.encode('utf-8')
        code = salt.encode('utf-8') + username
        activation_key = hashlib.sha1(code).hexdigest()
        user = User.objects.get(username=username)
        profile = user.profile
        profile.activation_key = activation_key
        profile.save()

        text_content = u'您好，' + username.decode('utf-8') + u'！恭喜您注册成功，请点击下面的链接激活您的账户：'
        activation_url = 'localhost:3000/teambuilder/user/activation/' + activation_key
        html_content = u'<b>激活链接：</b><a href="'+ activation_url +'">' + activation_url + '</a>'
        send_mail(subject, text_content, from_email, [to_email], html_message=html_content)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        RegisterView.mail_validate(username, email)
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

def ActivationView(request, activation_key):
    SHA_RE = re.compile('^[a-f0-9]{40}$')
    if SHA_RE.search(activation_key):
        try:
            user_profile = Profile.objects.get(activation_key=activation_key)
        except :
            return render('teamBuilder/activation/wrong_url.html')
        user = user_profile.owner
        user.is_active = True
        user.save()
        user_profile.activation_key = u'ALREADY_ACTIVATED'
        user_profile.save()
        return HttpResponseRedirect(reverse('teamBuilder:login'))
    else:
        return render_to_response('teamBuilder/activation/wrong_url.html')

class LoginView(FormView):
    template_name = 'teamBuilder/accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('teamBuilder:index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(LoginView, self).form_valid(form)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('teamBuilder:index'))

class IndexView(generic.TemplateView):
    template_name = 'teamBuilder/index.html'
