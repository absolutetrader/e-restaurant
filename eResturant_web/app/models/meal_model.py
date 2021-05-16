from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
from .booking_model import Booking

class Menu(models.Model):
    item_choices = (
        ("B", "Breakfast"),
        ("L", "Lunch"),
        ("D", "Dinner"),
    )
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=1, choices=item_choices)

    def __str__(self):
        return self.name + " (" + self.category + ") $" + str(self.price)


def calculateCost(userID):
    cost = 0
    for price in MealOrder.objects.all().filter(user=userID):
        cost += price.price

    return cost


class MealOrder(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=0)
    order = models.ForeignKey(Menu, on_delete=models.CASCADE, default=0)


