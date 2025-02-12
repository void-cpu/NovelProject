# Generated by Django 3.1.7 on 2021-03-09 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('UserName', models.CharField(max_length=20, null=True, verbose_name='用户名')),
                ('UserPwd', models.CharField(max_length=30, verbose_name='用户密码')),
                ('phone', models.CharField(max_length=20, unique=True, verbose_name='用户的手机号密码')),
            ],
            options={
                'verbose_name': '用户管理',
                'verbose_name_plural': '用户管理',
                'db_table': 'uneatable',
            },
        ),
        migrations.CreateModel(
            name='UserAnotherConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('isVip', models.BooleanField(default=False, verbose_name='是否是vip用户')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user.usermodel', verbose_name='用户')),
            ],
            options={
                'verbose_name': '用户扩展',
                'verbose_name_plural': '用户扩展',
            },
        ),
    ]
