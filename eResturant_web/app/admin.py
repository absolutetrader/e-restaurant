from django.contrib import admin

# Register your models here.
#from .models import userProfile, Booking, Table, Menu, MealOrder
from app.models.user_model import userProfile
from app.models.booking_model import Booking, Table
from app.models.meal_model import Menu, MealOrder

admin.site.register(userProfile)
admin.site.register(Booking)
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(MealOrder)
