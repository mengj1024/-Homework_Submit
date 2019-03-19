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
    path("老师首页/",views.teacher_home,name="老师首页"),
    path("Login_teacher/",views.teacherlogin,name="Login_teacher"),
    path("message/",views.message,name="message"),
    path("delete/",views.delete,name="delete"),
    # url(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT},name="hello"),
    # path('media/(.*?)',views.image,name="hello"),
    path('作业图片/',views.image,name="hello"),
    path('作业图片1/',views.test3,name="test3"),
    path("comment/",views.Test,name="comment"),
    path('comment2/',views.comments,name="comment2"),
    path("cheak/",views.Test2,name="Test2"),
    path("pigai/",views.pigai,name="批改"),
    path("test4/",views.pigai1,name="test4"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)