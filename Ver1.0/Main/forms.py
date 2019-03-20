from django.contrib.auth.forms import UserCreationForm
from .models import ID
from django import forms
from django.forms import fields,widgets,ModelForm
from .models import Grade,Student,Major,submitselectgrade
from django.http import request

class registerform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ID
        fields = ('username','email','nickname')

    
class TeacherLoginform(forms.Form):
    username = forms.CharField(max_length=50,label="用户名")
    password = forms.CharField(max_length=50,label="密码",widget=forms.PasswordInput)

#提交作业-选择班级
class submitselectgradeform(ModelForm):
    class Meta:
        model = submitselectgrade
        fields = ("major","grade")
   
#加入班级-选择专业
class Selectmajorform(forms.Form):
     gradename = fields.ChoiceField(
        choices = Major.objects.all().values_list('major_id','major_name'),
        widget = widgets.Select,
    )


#加入班级-选择班级
class Addgradeselectform(forms.Form):
    gradename = fields.ChoiceField(
        choices = Grade.objects.all().values_list('grade_id','grade_name'),
        widget = widgets.Select,
    )