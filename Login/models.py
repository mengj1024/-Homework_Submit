
import os

from django.db import models
from datetime import datetime
# Create your models here.

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass


class ImageUpload(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"作业名称")
    upload_time = models.DateTimeField(verbose_name=u"上传时间",default=datetime.now)


    class Meta:
        verbose_name = u"作业查看"
        verbose_name_plural = verbose_name
        db_table='Login_ImageUpload'


class Student(models.Model):
    nickname = models.CharField(max_length=50,verbose_name=u"学生姓名")
    add_time = models.DateTimeField(verbose_name=u"加入时间",default=datetime.now)
    class Meta:
        verbose_name = u"学生管理"    # 这个名字是显示在xadmin后台左侧栏中
        verbose_name_plural = verbose_name
        db_table = "Students_num"


class Teacher(models.Model):
    nickname = models.CharField(max_length=50,verbose_name=u"教师姓名")
    add_time = models.DateTimeField(verbose_name=u"加入时间",default=datetime.now)

    class Meta:
        verbose_name = "老师管理"
        verbose_name_plural = verbose_name
        db_table = "Teachers_num"

