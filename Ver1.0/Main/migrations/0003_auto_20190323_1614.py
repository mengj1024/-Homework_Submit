# Generated by Django 2.1.7 on 2019-03-23 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0002_auto_20190323_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_uploadname',
            field=models.OneToOneField(blank=True, null=True, on_delete=None, to='Main.Student', verbose_name='上传用户'),
        ),
    ]
