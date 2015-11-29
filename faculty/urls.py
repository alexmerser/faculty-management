"""faculty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django_downloadview.views.object import ObjectDownloadView

from assignments.models import AssignmentUpload
from auth.views import LoginView
from home.views import HomeView

from django.conf import settings
from django.conf.urls.static import static

download = ObjectDownloadView.as_view(model=AssignmentUpload, file_field='file')
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^courses/', include('courses.urls')),
    url(r'^researches/', include('research.urls')),
    url(r'^exams/', include('exams.urls')),
    url(r'^assignments/', include('assignments.urls')),
    url(r'^subjects/', include('subjects.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^login/$', LoginView.user_login, name='login'),
    url(r'^logout/$', LoginView.user_logout, name='logout'),
    url('^media/uploads/(?P<slug>[A-Za-z0-9_-]+)/$', download, name='download'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
