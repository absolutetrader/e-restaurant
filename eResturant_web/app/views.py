from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime


# Create your views here.
def home(request):
    return render(request, 'home.html', {})