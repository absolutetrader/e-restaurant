from django import forms
from django.conf import settings
from app.models.meal_model import MealOrder
from django.forms import ValidationError
from datetime import datetime, timedelta




class MealOrderForm(forms.ModelForm):
    
    class Meta:
        model = MealOrder
        fields = '__all__'
        exclude = ('booking',)