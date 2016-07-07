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
        text_content = u'您好，' + username + u'！恭喜您注册成功，请点击下面的链接激活您的账户：'
        html_content = u'<b>激活链接：</b><a href="www.baidu.com">www.baidu.com</a>'
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, 'text/html')
        msg.send()
        print("send email success!")

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        RegisterView.mail_validate(username, email)
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return super(RegisterView, self).form_valid(form)

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
