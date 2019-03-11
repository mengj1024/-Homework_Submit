from django.conf.urls import url
from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    # url('login/',views.login,name='login1'),
    path('upload/',views.upload,name='upload'), 
]