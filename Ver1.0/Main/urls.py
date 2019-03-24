from django.conf.urls import url,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


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
    url('Tou_1/',views.Tou_1,name=u"头脑风暴1"),
    url('create_grade/',views.creategrade,name=u'创建班级'),
    url('create_grade_name/',views.creategrade_name,name=u'创建班级名称'),
    url('Task_check/',views.task_check,name=u"作业批改"),
    url('teacher_sg/',views.teacher_sg,name=u'老师12'),
    # url('teacher_certain/',views.tracher_certain,name=u'老师确认班级'),
    url("teacher_a/",views.teacher_a,name=u'老师a页面'),
    url('teacher_b/',views.teacher_b,name=u"老师b页面"),
    url('teacher_c/',views.teacher_c,name=u"老师c页面"),
    url('teacher_d/',views.teacher_d,name=u"老师d界面"),
    url('teacher_e/',views.teacher_e,name=u"老师e界面"),
    url('teacher_f/',views.teacher_f,name=u"老师f界面"),
    url("teacherSub_s_1/",views.teacherSub_s_1,name=u'提交作业班级列表'),
    url("student_a/",views.studnet_a,name=u"学生a页面"),
    url("student_b/",views.student_b,name=u"学生b页面"),
    url("student_c/",views.student_c,name=u"学生c页面"),
    url("student_d/",views.student_d,name=u'学生d页面'),
    url("2333/",views.student_e,name=u"学生e页面"),
    url('SBT_1/',views.SBT,name=u'SBT1'),
    url("SBT_2/",views.SBT2,name=u'SBT2'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

