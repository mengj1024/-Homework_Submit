# Generated by Django 2.1.7 on 2019-03-16 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_auto_20190316_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='Answer',
            field=models.TextField(verbose_name='回答内容'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='Question',
            field=models.TextField(verbose_name='问题内容'),
        ),
    ]