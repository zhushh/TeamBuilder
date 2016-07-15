from django.http import HttpResponseRedirect
from django.views import generic
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.mail import send_mail, BadHeaderError, EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone
from rest_framework import viewsets, filters
from rest_framework.permissions import *
from .serializers import *
from .permissions import *
from .models import *
from .forms import *
import datetime
import hashlib
import random
import re

# Create your views here.

class UserProfileView(generic.TemplateView):
	template_name = 'teamBuilder/accounts/profile.html'

class TeamDetailView(generic.TemplateView):
	template_name = 'teamBuilder/team/team_detail.html'

class ProjectCreateView(generic.TemplateView):
	template_name = 'teamBuilder/project/create_project.html'

class TeamCreateView(generic.TemplateView):
	template_name = 'teamBuilder/team/create_team.html'

class ProjectManageView(generic.TemplateView):
	template_name = 'teamBuilder/project/manage_project.html'

class ProjectDetailView(generic.TemplateView):
	template_name = 'teamBuilder/project/project_detail.html'

class IndexView(generic.TemplateView):
    template_name = 'teamBuilder/index.html'

class RegisterView(generic.edit.FormView):
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
        return super(RegisterView, self).form_valid(form)

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
            return HttpResponseRedirect(reverse('teamBuilder:login'))
    else:
        context = {
            'err_msg': '错误的验证地址'
        }
        return render(request, 'teamBuilder/activation/msg.html', context)

class LoginView(generic.edit.FormView):
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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly, )

    def get_object(self):
        pk = self.kwargs.get('pk')

        if pk == "current":
            return self.request.user

        return super(UserViewSet, self).get_object()


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

class MessageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comments to be viewed or edited
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly, )

    def perform_create(self, serializer):
        user_profile = UserProfile.objects.filter(owner=self.request.user)[0]
        serializer.save(owner=user_profile)
