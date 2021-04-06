from django.db import models

# Create your models here.
class Table(models.Model):
    maxCapacity = models.IntegerField()
    isBooked = models.BooleanField(default='false')

class DateTime(models.Model):
    booking_start_time = models.DateTimeField()
    booking_end_time = models.DateTimeField()

class Booking(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    dateTime = models.ForeignKey(DateTime, on_delete=models.CASCADE)
