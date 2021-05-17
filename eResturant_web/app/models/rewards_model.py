from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
from django.db.models.deletion import CASCADE


class Rewards(models.Model):
    condition = models.IntegerField()
    discount = models.FloatField()
