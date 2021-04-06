from django.db import models

# Create your models here.
class Table(models.Model):
    maxCapacity = models.IntegerField()
    isBooked = models.BooleanField(default='false')

class Booking(models.Model):
    booking_start_time = models.DateTimeField(primary_key=True)
    booking_end_time = models.DateTimeField(primary_key=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)