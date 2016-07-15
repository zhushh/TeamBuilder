from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from .models import *
from .forms import *
import datetime
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

    def mail_validate(self, username, to_email):
        subject = u'Teambuilder用户验证'
        from_email = 'teambuilder@sina.com'
        # generate activation code
        salt = hashlib.sha1(str(random.random()).encode('utf-8')).hexdigest()[:5]
        username = username.encode('utf-8')
        code = salt.encode('utf-8') + username
        activation_key = hashlib.sha1(code).hexdigest()
        user = User.objects.get(username=username)
        profile = user.user_profile
        profile.activation_key = activation_key
        profile.save()

        text_content = u'<p>您好，' + username.decode('utf-8') + u'！恭喜您注册成功，请点击下面的链接激活您的账户：</p>'
        activation_url = self.request.get_host() + '/teambuilder/user/activation/' + activation_key
        html_content = text_content + u'<b>激活链接：</b><a href="'+ activation_url +'">' + activation_url + '</a>'
        send_mail(subject, '', from_email, [to_email], html_message=html_content)

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        user = form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        RegisterView.mail_validate(self, username, email)
        user = authenticate(username=username, password=password)
        login(self.request, user)
        # return super(RegisterView, self).form_valid(form)
        context = {
            'err_msg': '注册成功，请通过您的邮箱收到的验证邮件激活您的账号'
        }
        return render(self.request, 'teamBuilder/activation/msg.html', context)

def ActivationView(request, activation_key):
    SHA_RE = re.compile('^[a-f0-9]{40}$')
    if SHA_RE.search(activation_key):
        try:
            user_profile = UserProfile.objects.get(activation_key=activation_key)
        except :
            context = {
                'err_msg': '无效的验证地址'
            }
            return render(request, 'teamBuilder/activation/msg.html', context)
        user = user_profile.owner

        # check time expired
        expiration_date = datetime.timedelta(seconds=settings.EXPIRATION_TIME_DELTA)
        if (user.date_joined + expiration_date <= timezone.now()):
            context = {
                'err_msg': '该验证地址已过期，请重新注册'
            }
            user.delete()
            return render(request, 'teambuilder/activation/msg.html', context)
        else:
            user.is_active = True
            user.save()
            user_profile.activation_key = u'ALREADY_ACTIVATED'
            user_profile.save()
            # return HttpResponseRedirect(reverse('teamBuilder:login'))
            context = {
                'msg': '验证成功，5秒后跳转到登录页面'
            }
            return render(request, 'teambuilder/activation/success.html', context)
    else:
        context = {
            'err_msg': '错误的验证地址'
        }
        return render(request, 'teamBuilder/activation/msg.html', context)

class LoginView(FormView):
    template_name = 'teamBuilder/accounts/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('teamBuilder:index')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        print(self.request.get_host())
        return super(LoginView, self).form_valid(form)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('teamBuilder:index'))

class IndexView(generic.TemplateView):
    template_name = 'teamBuilder/index.html'
