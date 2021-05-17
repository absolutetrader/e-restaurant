from django.db import models
from django.conf import settings
from .booking_model import Booking


class InVoice(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=1)
    price = models.IntegerField()
