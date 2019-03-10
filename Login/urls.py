from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    url('register/', views.register, name='register'),
    # url('login/',views.login,name='login1'),
#     path('home/',views.home, name='home'),
]