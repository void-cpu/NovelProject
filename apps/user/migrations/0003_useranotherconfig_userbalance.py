# Generated by Django 3.1.7 on 2021-03-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210309_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='useranotherconfig',
            name='UserBalance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, max_length=10, verbose_name='用户余额'),
        ),
    ]