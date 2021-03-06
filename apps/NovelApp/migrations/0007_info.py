# Generated by Django 3.1.7 on 2021-03-06 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovelApp', '0006_auto_20210306_2236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('content', models.TextField(default='暂无章节内容', verbose_name='章节内容')),
                ('words', models.BigIntegerField(default=0, verbose_name='字数')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容',
                'ordering': ['-createTime', '-endTime'],
            },
        ),
    ]