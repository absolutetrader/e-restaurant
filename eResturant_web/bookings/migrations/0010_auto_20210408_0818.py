# Generated by Django 3.1.7 on 2021-04-08 08:18

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('bookings', '0009_auto_20210408_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.user'),
        ),
        migrations.AlterField(
            model_name='datetime',
            name='booking_end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 8, 18, 46, 169551)),
        ),
        migrations.AlterField(
            model_name='datetime',
            name='booking_start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 8, 18, 46, 169524)),
        ),
    ]
