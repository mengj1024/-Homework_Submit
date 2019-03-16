
import os

from django.db import models
from datetime import datetime
# Create your models here.

from django.contrib.auth.models import AbstractUser,User


class Grade(models.Model):
    # id = models.AutoField(primary_key=True)
    grade_name = models.CharField(max_length=50,verbose_name=u"班级名称",blank=True)
    grade_major = models.CharField(max_length=50,verbose_name=u'班级专业',blank=True)
    def __str__(self):
        return "%s-%s"%(self.grade_name,self.grade_major)

    class Meta:
        verbose_name = u"班级管理"
        verbose_name_plural = verbose_name
        db_table = "Grade_manage"

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    # Grades = models.ForeignKey(Grade,on_delete=models.CASCADE)
    # is_students = models.BooleanField(default=False)
    # is_teachers = models.BooleanField(default=False)
    

    class Meta(AbstractUser.Meta):
        pass

class ImageUpload(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"作业名称")
    img = models.ImageField(upload_to="")
    upload_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)
    upload_name = models.CharField(max_length=50,verbose_name=u"上传用户")
    def __str__(self):
        return "%s" %(self.upload_name)

    class Meta:
        verbose_name = u"作业查看"
        verbose_name_plural = verbose_name
        db_table='Login_ImageUpload'
        pass

# class add_grades(models.Model):
#     grade_name = models.CharField(max_length=50,verboser_name=u"班级名称")

class Student(models.Model):
    nickname = models.CharField(max_length=50,verbose_name=u"学生姓名")
    add_time = models.DateTimeField(verbose_name=u"加入时间",default=datetime.now)
    students_name = models.OneToOneField("User",on_delete=models.CASCADE)
    students_home = models.OneToOneField("ImageUpload",on_delete=models.CASCADE)
    stu_chengji = models.OneToOneField("chengji",on_delete=models.CASCADE)
    students_grade = models.ForeignKey("Grade",on_delete=models.CASCADE)
    students_teacher = models.ManyToManyField("Teacher")
    # Grade = models.ForeignKey("Teacher",on_delete=models.CASCADE)
    def __str__(self):
        return "%s"%(self.stu_chengji)
    class Meta:
        verbose_name = u"学生管理"    # 这个名字是显示在xadmin后台左侧栏中
        verbose_name_plural = verbose_name
        db_table = "Students_num"

class Teacher(models.Model):
    nickname = models.CharField(max_length=50,verbose_name=u"教师姓名")
    add_time = models.DateTimeField(verbose_name=u"加入时间",default=datetime.now)
    teacher_name = models.OneToOneField("User",on_delete=models.CASCADE)

    teacher_grade = models.ManyToManyField("Grade")
    # teacher_stu = models.ManyToManyField("Student")
    def __str__(self):
        return "%s"%(self.teacher_name)
    class Meta:
        verbose_name = "老师管理"
        verbose_name_plural = verbose_name
        db_table = "Teachers_num"

from django import forms
class TeacherloginForm(forms.Form):
    username = forms.CharField(max_length=50,label="用户名")
    password = forms.CharField(max_length=50,label="密码")

class Chengji(models.Model):
    chengji_Type = models.CharField(max_length=5,verbose_name=u"成绩")
    def __str__(self):
        return "%s"%(self.chengji_Type)
    class Meta:
        verbose_name = "成绩分级"
        verbose_name_plural = verbose_name
        db_table = "Chengji"


class Questions(models.Model):
    Question = models.TextField(verbose_name=u"问题内容")
    def __str__(self):
        return "%s"%(self.Question)
    class Meta:
        verbose_name="问题内容"
        verbose_name_plural=verbose_name
        db_table="Questions"

class Answers(models.Model):
    Answer_name = models.CharField(max_length=50,verbose_name=u"回答者")
    Answer_time = models.DateTimeField(verbose_name=u"回答时间",default=datetime.now)
    Answer      = models.TextField(verbose_name=u"回答内容")
    def __str__(self):
        return "%s的回答为-----:%s"%(self.Answer_name,self.Answer)
    class Meta:
        verbose_name="回答内容"
        verbose_name_plural=verbose_name
        db_table="Answer"

import django_comments
from django_comments.models import Comment
# class upload_comment(models.Model):
#     user = request.user
#     text = request.POST.get('text',"")