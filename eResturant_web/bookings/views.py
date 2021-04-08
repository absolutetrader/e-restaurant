from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking

# Create your views here.


def bookings_view(request, *args, **kwargs):
    obj = Booking.objects.get(id=5)
    my_context = {
        'object': obj
    }
    return render(request, 'bookings.html', my_context)
