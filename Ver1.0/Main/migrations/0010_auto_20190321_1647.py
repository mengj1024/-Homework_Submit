# Generated by Django 2.1.7 on 2019-03-21 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0009_auto_20190321_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_grade',
            field=models.ManyToManyField(to='Main.abc', verbose_name='班级'),
        ),
    ]
