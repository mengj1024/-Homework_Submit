import xadmin
from .models import User,ImageUpload,Student,Teacher,Grade,Chengji,Questions,Answers
from xadmin import views

class UserAdmin(object):
    # show_detail_fields=['user_name']
    pass
    
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(views.BaseAdminView,BaseSetting)

class GradeAdmin(object):
    pass
    list_display = ["id","grade_name",'grade_major']
xadmin.site.register(Grade,GradeAdmin)

class ImageUploadAdmin(object):
    pass
    list_display = ["name","upload_time",'upload_name']  # 显示的列
    show_detail_fields=["id"]
    show_bookmarks=False
    search_fields = ['upload_name']
    ordering = ['upload_time',] 
    # fields = ['name']
    # search_fields = ("")   # 搜索字段
    # list_filter = ("")     # 筛选字段
    # readonly_fields = ['']  # 只读字段
    # model_icon = "fa fa-music" # 小图标
xadmin.site.register(ImageUpload,ImageUploadAdmin)

class StudentAdmin(object):
    pass
    list_display = ["id","nickname","add_time"]
xadmin.site.register(Student,StudentAdmin)

class TeacherAdmin(object):
    pass
    list_display = ["id","nickname",'add_time']
xadmin.site.register(Teacher,TeacherAdmin)

class GlobalSetting(object):
    site_title = "后台管理系统"
    site_footer = "2019"
    menu_style = "accordion"    # 折叠左侧菜单栏
xadmin.site.register(views.CommAdminView,GlobalSetting)

class ChengjiAdmin(object):
    pass
xadmin.site.register(Chengji,ChengjiAdmin)

class QuestionsAdmin(object):
    pass
xadmin.site.register(Questions,QuestionsAdmin)

class AnswersAdmin(object):
    pass
xadmin.site.register(Answers,AnswersAdmin)