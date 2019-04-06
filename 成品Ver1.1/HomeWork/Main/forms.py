from django.contrib.auth.forms import UserCreationForm
from .models import ID
from django import forms
from django.forms import fields,widgets,ModelForm
from .models import Grade,Student,Major,submitselectgrade,abc,Teacher
from django.http import request

class registerform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ID
        fields = ('username','email','nickname')

    
class TeacherLoginform(forms.Form):
    username = forms.CharField(max_length=50,label="用户名")
    password = forms.CharField(max_length=50,label="密码",widget=forms.PasswordInput)


class submitselectgradeform(forms.Form):
    gradename = forms.ModelChoiceField(queryset=Student.objects.all().values_list("student_user","abc_stu"))
  


#加入班级-选择专业
class Selectmajorform(forms.Form):
    gradename = forms.ModelChoiceField(queryset=abc.objects.all())
    widget = widgets.Select,


#加入班级-选择班级
class Addgradeselectform(forms.Form):
    gradename = fields.ChoiceField(
        choices = Grade.objects.all().values_list('grade_id','grade_name'),
        widget = widgets.Select,
    )

#批改作业-选择班级
class Teacherselectgradeform(forms.Form):
        gradename = forms.ModelChoiceField(queryset=Teacher.objects.all())
