# Generated by Django 3.2.17 on 2024-03-01 11:17

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_remove_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='completion_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 11, 15, 41, 870294, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='modified_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 1, 11, 15, 41, 870294, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='task',
            name='task_status',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
