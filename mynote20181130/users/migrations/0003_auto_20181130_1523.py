# Generated by Django 2.0.6 on 2018-11-30 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_last_login_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default='1996-01-01', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='graduate_time',
            field=models.CharField(default='2000-10-10', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='id_number',
            field=models.CharField(default='11010819990121682', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(default='工程师', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='job_2',
            field=models.CharField(default='员工', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='job_join_time',
            field=models.CharField(default='2009-10-10', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='job_number',
            field=models.CharField(default='0001', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='job_time',
            field=models.CharField(default='2015-10-31', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='第一次登录', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='18211083025', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='school',
            field=models.CharField(default='河北燕山大学', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='sex',
            field=models.CharField(default='女', max_length=3),
        ),
        migrations.AddField(
            model_name='user',
            name='team_belong',
            field=models.CharField(default='C001', max_length=20),
        ),
        migrations.AddField(
            model_name='user',
            name='xue_li',
            field=models.CharField(default='本科', max_length=30),
        ),
        migrations.AddField(
            model_name='user',
            name='zhengzhi_mianmao',
            field=models.CharField(default='群众', max_length=10),
        ),
        migrations.AddField(
            model_name='user',
            name='zhengzhi_time',
            field=models.CharField(default='2010-10-31', max_length=20),
        ),
    ]
