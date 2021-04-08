# Generated by Django 3.1.7 on 2021-04-08 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0015_auto_20210408_0824'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DateTime',
            new_name='bookingDateTime',
        ),
        migrations.AlterField(
            model_name='booking',
            name='dateTime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
