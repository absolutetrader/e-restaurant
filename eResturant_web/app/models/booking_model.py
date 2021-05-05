from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE



class Table(models.Model):
    maxCapacity = models.IntegerField()


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, null=True)
    bookingStartDateTime = models.DateTimeField(default=datetime.now)
    bookingEndDateTime = models.DateTimeField(default=datetime.now)
    guests = models.IntegerField(default=1)
