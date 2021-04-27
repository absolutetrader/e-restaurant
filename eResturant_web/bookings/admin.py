from django.contrib import admin

# Register your models here.
from .models import Table
from .models import Booking

admin.site.register(Table)
admin.site.register(Booking)