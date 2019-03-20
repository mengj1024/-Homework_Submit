import xadmin
from xadmin import views

class BaseSetting(object):
    enable_themes=True
    use_bootswatch=True
xadmin.site.register(views.BaseAdminView,BaseSetting)



from .models import Student,Teacher,Score,Task,Major,Grade

class StudentAdmin(object):
    pass
xadmin.site.register(Student,StudentAdmin)

class TeacherAdmin(object):
    pass
xadmin.site.register(Teacher,TeacherAdmin)

class ScoreAdmin(object):
    pass
xadmin.site.register(Score,ScoreAdmin)

class TaskAdmin(object):
    pass
xadmin.site.register(Task,TaskAdmin)

class MajorAdmin(object):
    pass
xadmin.site.register(Major,MajorAdmin)

class GradeAdmin(object):
    pass
xadmin.site.register(Grade,GradeAdmin)

class GlobalSetting(object):
    site_title = "毕业设计后台管理"
    site_footer = "2019"
    menu_style = "accordion"    # 折叠左侧菜单栏
xadmin.site.register(views.CommAdminView,GlobalSetting)