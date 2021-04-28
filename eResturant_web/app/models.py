from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE
# Create your models here.


class userProfile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    fName = models.CharField(max_length=50, name="First Name")
    lName = models.CharField(max_length=50, name="Last Name")
    isStaff = models.BooleanField(default=False)


"""class Menu(forms.ModelForm):
    
    MENU = (
        (
            '0', 'Alfredo Chicken Pasta',
            '1', 'Spaghetti Bolognese',
            '2', 'Chicken Pizza',
            '3', 'Vegetarian Pizza',
            '4', 'Coke'
        )
    )"""
