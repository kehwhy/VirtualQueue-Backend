# Generated by Django 3.1.5 on 2021-01-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualqueueapi', '0003_auto_20210123_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]