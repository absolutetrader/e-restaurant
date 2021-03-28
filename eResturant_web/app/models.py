from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError
# Create your models here.

class User(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    isStaff = models.BooleanField()
    email = models.EmailField()

    def __unicode__(self):
        return self.email
