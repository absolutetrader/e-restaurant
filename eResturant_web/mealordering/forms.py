from django import forms
from django.contrib import admin
from django.db import models
from bookings.models import models
import mealordering.models
from app.models import models

class MealOrderForm(forms.ModelForm):
    class Meta:
        model = mealordering.models.MealOrder
        fields = '__all__'


