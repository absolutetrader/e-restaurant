from django.contrib import admin

# Register your models here.
from .models import Menu, MealOrder

admin.site.register(Menu)
admin.site.register(MealOrder)
