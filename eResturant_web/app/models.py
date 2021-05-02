from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
# Create your models here.

# login/signup


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    fName = models.CharField(max_length=50, name="First Name")
    lName = models.CharField(max_length=50, name="Last Name")
    isStaff = models.BooleanField(default=False)
###############


# table booking
class Table(models.Model):
    maxCapacity = models.IntegerField()
    isBooked = models.BooleanField(default=False)


class Booking(models.Model):
    user = models.ForeignKey(
        userProfile, on_delete=models.CASCADE, default=1)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default="")
    bookingStartDateTime = models.DateTimeField(default=datetime.now)
    bookingEndDateTime = models.DateTimeField(default=datetime.now)
    guests = models.IntegerField(default=1)
######################


# meal ordering
class Menu(models.Model):
    item_choices = (
        ("E", "Entree"),
        ("M", "Main"),
        ("D", "Dessert"),
        ("+", "Extra(s)")
    )
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    category = models.CharField(max_length=1, choices=item_choices)


def calculateCost(userID):
    cost = 0
    for price in MealOrder.objects.all().filter(user=userID):
        cost += price.price

    return cost


class MealOrder(models.Model):
    table = models.ForeignKey(
        Table, on_delete=models.CASCADE, default=0)
    order = models.ForeignKey(
        Menu, on_delete=models.CASCADE, default=0)
