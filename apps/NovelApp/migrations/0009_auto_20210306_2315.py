# Generated by Django 3.1.7 on 2021-03-06 23:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('NovelApp', '0008_chapter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chapter',
            options={'ordering': ['-createTime', '-endTime'], 'verbose_name': '章节', 'verbose_name_plural': '章节'},
        ),
    ]