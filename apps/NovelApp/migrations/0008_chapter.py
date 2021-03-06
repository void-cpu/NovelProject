# Generated by Django 3.1.7 on 2021-03-06 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NovelApp', '0007_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('endTime', models.DateTimeField(auto_now=True, verbose_name='最后编辑时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=128, unique=True, verbose_name='章节标题')),
                ('Info', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='NovelApp.info', verbose_name='文章内容id')),
                ('Novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='NovelApp.novel', verbose_name='小说ID')),
            ],
            options={
                'verbose_name': '内容',
                'verbose_name_plural': '内容',
                'ordering': ['-createTime', '-endTime'],
            },
        ),
    ]