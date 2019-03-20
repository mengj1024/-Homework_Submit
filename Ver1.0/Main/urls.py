from django.conf.urls import url,include
from . import views


app_name="Main"
urlpatterns=[
    url('register/',views.register,name=u'学生注册'),
    # url('login/',views.login,name=u'登陆'),
    url('teacher_login/',views.TeacherLogin,name=u'老师登陆'),
    url('teacher_home/',views.TeacherHome,name=u'老师主页'),
    url('task_upload/',views.Taskupload_view,name=u'作业上传'),
    url('upload/',views.TaskUpload,name=u'上传功能'),
    url('task-success/',views.Taakupload_success,name=u'上传成功'),
    url('select_grade/',views.Submit_select_grade,name=u'选择班级'),
    url('selected_grade/',views.ChoicedGrade,name=u'班级已选择'),
    url('add_grade/',views.add_grade,name=u'加入班级'),
    url('add_major/',views.add_major,name=u'加入专业'),
    url('add_grade_succeed/',views.add_grade_select,name=u'加入班级选择成功'),
]
