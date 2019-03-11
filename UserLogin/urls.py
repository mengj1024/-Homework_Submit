"""UserLogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from Login import views
# urlpatterns = [
#     url('admin/', admin.site.urls),
#     # 别忘记在顶部引入 include 函数
#     url('users/', include('Login.urls')),
#     url('users/', include('django.contrib.auth.urls')),
#     # url('', views.home, name='home'),
# ]

from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
import xadmin

urlpatterns = [
    # url('admin/', admin.site.urls),
    path('xadmin/',xadmin.site.urls),
    url('users/', include('Login.urls')),
    url('users/', include('django.contrib.auth.urls')),
    # path('home/',views.home, name='home'),
    # url('',views.home, name='home'),
    url('',views.home, name='home'),

]    