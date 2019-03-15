from django.conf.urls import url
from . import views
from django.urls import path
import xadmin
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

app_name = 'users'
urlpatterns = [
    path('register/', views.register, name='register'),
    # url('login/',views.login,name='login1'),
    path('upload/',views.upload,name='upload'), 
    path('Students_message/',views.Students_message,name="学生信息"),
    path("Homework_ck/",views.Homework_ck,name="作业批改"),
    path("Tou/",views.Tou,name="头脑风暴"),
    path("Login_teacher/",views.teacherlogin,name="Login_teacher"),
    path("message/",views.message,name="message"),
    path("delete/",views.delete,name="delete"),
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT},name="hello"),
    # path('media/(.*?)',views.image,name="hello"),
    path('media/',views.image,name="hello"),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)