# Generated by Django 3.1.7 on 2021-03-06 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='作者名'),
        ),
    ]
