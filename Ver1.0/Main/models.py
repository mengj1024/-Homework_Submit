from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from datetime import datetime

class ID(AbstractUser):
    # 用户的ID
    # user_id = models.AutoField(primary_key=True)
    # 用户的昵称
    nickname = models.CharField(max_length=50,verbose_name=u'昵称',blank=True)
    # 用户的头像
    # user_img = models.ImageField(blank=True)
    class  Meta(AbstractUser.Meta):
        pass
    

class Student(models.Model):
    student_id = models.BigAutoField(primary_key =True) #学生id
    student_user = models.OneToOneField('ID',on_delete=None,verbose_name=u'账户') #学生对应的账户
    # student_teacher = models.ForeignKey('Teacher',blank=True,null=True,on_delete=None,verbose_name=u'老师') #学生的老师
    # student_grade   = models.ManyToManyField('Grade',blank=True,null=True,verbose_name=u'班级') #学生班级
    abc_stu = models.ManyToManyField("abc",null=True,blank=True)
    # stu_task = models.OneToOneField("Task",on_delete=None,blank=True,null=True)
    # stu_grade   = models.ForeignKey("abc",on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return '%s'%(self.student_user)
    class Meta:
        verbose_name = u"学生管理"
        verbose_name_plural = verbose_name
        db_table = "Student_manage"

class Teacher(models.Model):
    teacher_id = models.BigAutoField(primary_key=True) #老师id
    teacher_user = models.OneToOneField('ID',on_delete=None,verbose_name=u'账户') #老师对的的账户
    teacher_grade = models.ManyToManyField("abc",verbose_name=u'班级',blank=True) #老师对应的班级，多对多
    def __str__(self):
        return "%s"%(self.teacher_user)
    class Meta:
        verbose_name = u"老师管理"
        verbose_name_plural = verbose_name
        db_table = "Teacher_manage"

class Score(models.Model):
    score_id = models.BigAutoField(primary_key=True) #成绩的id
    score    = models.CharField(max_length=10,null=True,verbose_name=u'成绩') #成绩登记
    def __str__(self):
        return "%s"%(self.score)
    class Meta:
        verbose_name = u"成绩"
        verbose_name_plural = verbose_name
        db_table = "Score"

class Task(models.Model):
    task_id = models.BigAutoField(primary_key=True) #作业的id
    task_uploadtime = models.DateTimeField(default=datetime.now,verbose_name=u'上传时间') #作业上传的时间
    task_uploadname = models.OneToOneField("Student",on_delete=None,null=True,blank=True,verbose_name=u"上传用户")
    # task_uploadstu  = models.OneToOneField("Student",on_delete=None,verbose_name=u'上传的学生') #作业上传的学生
    task_score      = models.OneToOneField("Score",on_delete=None,null=True,blank=True,verbose_name=u'作业分数') #作业分数
    task_upload     = models.ImageField(upload_to="作业/")
    task_grade      = models.ForeignKey("abc",verbose_name=u"作业的班级",on_delete=models.CASCADE)
    task_comment = models.CharField(max_length=500,null=True,blank=True)
    task_img = models.TextField(max_length=16000,null=True,blank=True)
    def __str__(self):
        return "%s"%(self.task_upload)
    class Meta:
        verbose_name = u"作业管理"
        verbose_name_plural = verbose_name
        db_table = "Task_manage"


class Major(models.Model):
    major_id = models.BigAutoField(primary_key=True) #专业id
    major_name = models.CharField(max_length=50,verbose_name=u'专业名字') #专业名字
    # major_grade = models.ForeignKey("Grade",on_delete=models.PROTECT,null=True,blank=True)
    grade_name = models.CharField(max_length=50,)
    def __str__(self):
        return '%s'%(self.grade_name)
    class Meta:
        verbose_name = u"专业管理"
        verbose_name_plural = verbose_name
        db_table = "Major_manage"

class Grade(models.Model):
    grade_id =models.BigAutoField(primary_key=True) #班级id
    grade_name = models.CharField(max_length=50,verbose_name=u'班级名字') #班级名字
    # stu_name   = models.ForeignKey('Student',null=True,blank=True,verbose_name=u'学生',on_delete=models.PROTECT)
    # grade_major = models.Field("Major",on_delete=None,verbose_name=u'班级专业') #班级专业
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
    chioces = models.ForeignKey("Student",on_delete=None,null=True)


class abc(models.Model):
    abc_id =  models.BigAutoField(primary_key=True)
    abc_name = models.CharField(max_length=50,verbose_name=u'班级名字')
    # abc_stu  = models.ForeignKey("Student",on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return '%s'%(self.abc_name)
    # def get_absolute_url(self):
    #     return 'grade/%s.html'
    class Meta:
        verbose_name = u"班级管理2"
        verbose_name_plural = verbose_name
        db_table = "Grade_manage2"

class Question(models.Model):
    question_id = models.BigAutoField(primary_key=True)
    question    = models.CharField(max_length=500,verbose_name=u'问题内容')
    question_who = models.OneToOneField("Teacher",on_delete=None)
    question_grade = models.OneToOneField("abc",on_delete=None,null=True,blank=True)
    # question_answer= models.ForeignKey("Answer",on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self):
        return '%s'%(self.question)
    class Meta:
        verbose_name=u'头脑风暴'
        verbose_name_plural = verbose_name
        db_table = "Questions"

class Answer(models.Model):
    answer_id = models.BigAutoField(primary_key=True)
    answer    = models.CharField(max_length=500,verbose_name=u'回答内容')
    answer_who= models.OneToOneField("ID",on_delete=None)
    question = models.ForeignKey("Question",on_delete=models.CASCADE,null=True,blank=True)
    answer_grade = models.ForeignKey("abc",on_delete=None,null=True,blank=True)
    def __str__(self):
        return "%s"%(self.answer)
    class Meta:
        verbose_name=u'回复查看'
        verbose_name_plural=verbose_name
        db_table="Answers"
