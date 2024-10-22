# Generated by Django 3.1.7 on 2021-03-06 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NovelApp', '0005_novelclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-createTime', '-endTime'], 'verbose_name': '作者信息', 'verbose_name_plural': '作者信息'},
        ),
        migrations.AlterModelOptions(
            name='novelclass',
            options={'ordering': ['-createTime', '-endTime'], 'verbose_name': '小说类型', 'verbose_name_plural': '小说类型'},
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='小说名')),
                ('desc', models.CharField(default='暂无简介信息', max_length=256, verbose_name='简介')),
                ('Author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NovelApp.author', verbose_name='作者')),
                ('NovelClass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NovelApp.novelclass', verbose_name='小说类型')),
            ],
            options={
                'verbose_name': '小说',
                'verbose_name_plural': '小说',
                'ordering': ['-createTime', '-endTime'],
            },
        ),
    ]
