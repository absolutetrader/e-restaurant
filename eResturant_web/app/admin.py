from django.contrib import admin

# Register your models here.
from .models import userProfile, Booking, Table, Menu, MealOrder

admin.site.register(userProfile)
admin.site.register(Booking)
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(MealOrder)
