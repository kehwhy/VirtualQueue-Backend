# Generated by Django 3.1.5 on 2021-01-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualqueueapi', '0005_auto_20210123_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
    ]
