from django.shortcuts import render
from django.http import HttpResponse
from app.models.booking_model import Booking
from app.forms.booking_forms import BookingForm, editBookingForm

# Create your views here.


def bookings_view(request, *args, **kwargs):
    obj = Booking.objects.all()
    my_context = {
        'object': obj
    }
    return render(request, 'app/bookings.html', my_context)


def booking_create_view(request, *args, **kwargs):
    form = BookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'app/bookings_create.html', context)


def booking_edit_view(request, *args, **kwargs):
    form = editBookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'app/bookings_edit.html', context)
