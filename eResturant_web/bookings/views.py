from django.shortcuts import render
from django.http import HttpResponse
from .models import Booking
from .forms import BookingForm

# Create your views here.


def booking_create_view(request):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'booking_create.html', context)


def bookings_view(request, *args, **kwargs):
    obj = Booking.objects.get(id=5)
    my_context = {
        'object': obj
    }
    return render(request, 'bookings.html', my_context)
