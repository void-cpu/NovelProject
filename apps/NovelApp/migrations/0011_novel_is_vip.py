# Generated by Django 3.1.7 on 2021-03-07 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NovelApp', '0010_auto_20210306_2322'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='is_vip',
            field=models.BooleanField(default=False, verbose_name='是否vip 收费'),
        ),
    ]
