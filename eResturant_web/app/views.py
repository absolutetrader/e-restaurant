from django.shortcuts import render
from django.http import HttpResponse
import re
from django.utils.timezone import datetime


# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    return render(
        request,
        'app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
