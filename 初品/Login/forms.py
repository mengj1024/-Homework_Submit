from django.contrib.auth.forms import UserCreationForm
from .models import User,Chengji

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")

#coding=utf-8
from django import forms
class TeacherloginForm(forms.Form):
    username = forms.CharField(max_length=50,label="用户名")
    password = forms.CharField(max_length=50,label="密码",widget=forms.PasswordInput)

from django.forms import fields,widgets

class PiGaiForm(forms.Form):
    grade = fields.ChoiceField(
        # choices=[
        #     (1,"A"),
        #     (2,"B"),
        #     (3,"C"),
        # ]
        choices=Chengji.objects.all().values_list("id","chengji_Type"),
        widget=widgets.Select,
    )