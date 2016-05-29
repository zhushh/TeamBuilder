"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin


from django.contrib.auth.models import User
from rest_framework import routers
from . import views
from api import views as api_views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'profiles', api_views.ProfileViewSet)
router.register(r'projects', api_views.ProjectViewSet)
router.register(r'teams', api_views.TeamViewSet)
router.register(r'comments', api_views.CommentViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^logout/$', views.LogoutView, name='logout'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^', include('teamBuilder.urls')),
]
