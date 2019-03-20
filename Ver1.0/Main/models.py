from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from datetime import datetime

class ID(AbstractUser):
    # 用户的ID
    # user_id = models.AutoField(primary_key=True)
    # 用户的昵称
    nickname = models.CharField(max_length=50,verbose_name=u'昵称')
    # 用户的头像
    # user_img = models.ImageField(blank=True)
    class  Meta(AbstractUser.Meta):
        pass
    

class Student(models.Model):
    student_id = models.BigAutoField(primary_key =True) #学生id
    student_user = models.OneToOneField('ID',on_delete=None,verbose_name=u'账户') #学生对应的账户
    student_teacher = models.ForeignKey('Teacher',blank=True,null=True,on_delete=None,verbose_name=u'老师') #学生的老师
    student_grade   = models.ManyToManyField('Grade',blank=True,null=True,verbose_name=u'班级') #学生班级

    def __str__(self):
        return '%s'%(self.student_user)
    class Meta:
        verbose_name = u"学生管理"
        verbose_name_plural = verbose_name
        db_table = "Student_manage"

class Teacher(models.Model):
    teacher_id = models.BigAutoField(primary_key=True) #老师id
    teacher_user = models.OneToOneField('ID',on_delete=None,verbose_name=u'账户') #老师对的的账户
    teacher_grade = models.ManyToManyField("Grade",verbose_name=u'班级') #老师对应的班级，多对多
    
    class Meta:
        verbose_name = u"老师管理"
        verbose_name_plural = verbose_name
        db_table = "Teacher_manage"

class Score(models.Model):
    score_id = models.BigAutoField(primary_key=True) #成绩的id
    score    = models.CharField(max_length=10,null=True,verbose_name=u'成绩') #成绩登记

    class Meta:
        verbose_name = u"成绩"
        verbose_name_plural = verbose_name
        db_table = "Score"

class Task(models.Model):
    task_id = models.BigAutoField(primary_key=True) #作业的id
    task_uploadtime = models.DateTimeField(default=datetime.now,verbose_name=u'上传时间') #作业上传的时间
    task_uploadname = models.CharField(max_length=50,verbose_name=u"上传用户")
    # task_uploadstu  = models.OneToOneField("Student",on_delete=None,verbose_name=u'上传的学生') #作业上传的学生
    task_score      = models.OneToOneField("Score",on_delete=None,null=True,blank=True,verbose_name=u'作业分数') #作业分数
    task_upload     = models.ImageField(upload_to="作业/")
    task_grade      = models.ForeignKey("Grade",verbose_name=u"作业的班级",on_delete=models.CASCADE)

    class Meta:
        verbose_name = u"作业管理"
        verbose_name_plural = verbose_name
        db_table = "Task_manage"


class Major(models.Model):
    major_id = models.BigAutoField(primary_key=True) #专业id
    major_name = models.CharField(max_length=50,verbose_name=u'专业名字') #专业名字
    def __str__(self):
        return '%s'%(self.major_name)
    class Meta:
        verbose_name = u"专业管理"
        verbose_name_plural = verbose_name
        db_table = "Major_manage"

class Grade(models.Model):
    grade_id =models.BigAutoField(primary_key=True) #班级id
    grade_name = models.CharField(max_length=50,verbose_name=u'班级名字') #班级名字
    stu_name   = models.ManyToManyField('Student',null=True,blank=True,verbose_name=u'学生')
    grade_major = models.ForeignKey("Major",on_delete=None,verbose_name=u'班级专业') #班级专业
    def __str__(self):
        return '%s'%(self.grade_name)
    # def get_absolute_url(self):
    #     return 'grade/%s.html'
    class Meta:
        verbose_name = u"班级管理"
        verbose_name_plural = verbose_name
        db_table = "Grade_manage"

#提交作业-选择班级表单
class submitselectgrade(models.Model):
    major = models.ForeignKey("Major",on_delete=models.CASCADE,null=True)
    grade = models.ForeignKey("grade",on_delete=models.CASCADE,null=True)