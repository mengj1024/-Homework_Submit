# Generated by Django 2.1.7 on 2019-03-21 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='abc_stu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Main.Student'),
        ),
    ]
