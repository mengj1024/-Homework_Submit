# Generated by Django 2.1.7 on 2019-03-24 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0004_auto_20190324_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answer_grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=None, to='Main.abc'),
        ),
    ]
