# Generated by Django 3.1.7 on 2021-04-08 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0017_auto_20210408_0828'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='bookingEndTime',
            new_name='bookingEndDateTime',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='bookingStartTime',
            new_name='bookingStartDateTime',
        ),
    ]
