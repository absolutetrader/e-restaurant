from django.db import models
from bookings import models
from app.models import models
from django.contrib.auth.models import User
# Create your models here.


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
        'bookings.Table', on_delete=models.CASCADE, default="")
    order = models.ForeignKey(Menu, on_delete=models.CASCADE, default="")
