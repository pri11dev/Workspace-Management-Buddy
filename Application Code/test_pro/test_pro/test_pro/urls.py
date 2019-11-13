"""test_pro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from test_app import views
from django.conf.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    re_path('^accounts/', views.user_login),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^home/',include('test_app.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^meeting/',include('Meeting.urls')),
    url(r'^re/',include('recreational.urls')),
    url(r'next/',views.index1),
    url(r'next1/',views.index2),
    

] 