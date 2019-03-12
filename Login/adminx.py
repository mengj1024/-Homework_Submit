import xadmin
from .models import User,ImageUpload,Student,Teacher
from xadmin import views

class UserAdmin(object):
    pass

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

xadmin.site.register(views.BaseAdminView,BaseSetting)

class ImageUploadAdmin(object):
    pass
    list_display = ["id","upload_time","name"]  # 显示的列
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

