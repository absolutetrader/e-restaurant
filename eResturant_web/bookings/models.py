from django.db import models
from app.models import models
from datetime import datetime
# Create your models here.


class Table(models.Model):
    maxCapacity = models.IntegerField()
    isBooked = models.BooleanField(default=False)


class Booking(models.Model):
    user = models.ForeignKey(
        'app.userProfile', on_delete=models.CASCADE, default=1)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="")
    bookingStartDateTime = models.DateTimeField(default=datetime.now)
    bookingEndDateTime = models.DateTimeField(default=datetime.now)
    guests = models.IntegerField(default=1)
