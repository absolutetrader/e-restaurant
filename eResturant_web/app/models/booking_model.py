from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
from .user_model import userProfile


class Table(models.Model):
    maxCapacity = models.IntegerField()
    isBooked = models.BooleanField(default=False)


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="")
    bookingStartDateTime = models.DateTimeField(default=datetime.now)
    bookingEndDateTime = models.DateTimeField(default=datetime.now)
    guests = models.IntegerField(default=1)
