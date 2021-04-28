from django.db import models
from bookings.models import models
from app.models import models
from django.contrib.auth.models import User
# Create your models here.
class MealOrder(models.Model):
    user = models.ForeignKey('app.userProfile', on_delete=models.CASCADE, default=1)
    table = models.ForeignKey('bookings.Table', on_delete=models.CASCADE, default="")

