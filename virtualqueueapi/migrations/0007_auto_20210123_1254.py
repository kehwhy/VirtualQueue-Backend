# Generated by Django 3.1.5 on 2021-01-23 17:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('virtualqueueapi', '0006_auto_20210123_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=100, primary_key=True, serialize=False, unique=True),
        ),
    ]