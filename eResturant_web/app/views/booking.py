from django.shortcuts import render
from django.http import HttpResponse
from app.models.booking_model import Booking, Table
from app.forms.booking_forms import InitialBookingForm, editBookingForm, FinalBookingForm
import datetime
from django.shortcuts import redirect
import json
from json import JSONEncoder


# Create your views here.


def bookings_view(request, *args, **kwargs):
    obj = Booking.objects.all()
    my_context = {
        'object': obj
    }
    return render(request, 'app/bookings.html', my_context)

def booking_create_view(request):
    
    initial_form = InitialBookingForm(request.POST or None)
    current_user = request.user
    if initial_form.is_valid():
        f = initial_form.save(commit=False)
        f.user = current_user
        f.save()
        current_guests = initial_form.cleaned_data['guests']
        current_start_datetime = initial_form.cleaned_data['bookingStartDateTime']
        current_end_datetime = initial_form.cleaned_data['bookingEndDateTime']
        request.session['current_guests'] = current_guests
        request.session['current_start_datetime'] = json.dumps(current_start_datetime, cls=DateTimeEncoder)
        request.session['current_end_datetime'] = json.dumps(current_end_datetime, cls= DateTimeEncoder)
        return redirect("bookings/create/table")   
            
            
      
    return render(request, 'app/bookings_create.html', { 'initial_form' : initial_form})

def booking_create_table_view(request):
    
    table_form = FinalBookingForm(request.POST, guests = request.session.get('current_guests'), booking_start_date_time = json.loads(request.session.get('current_start_datetime'), object_hook=DecodeDateTime), booking_end_date_time = json.loads(request.session.get('current_end_datetime'), object_hook=DecodeDateTime))
    if request.method == "POST":
        table_form = FinalBookingForm(request.POST, guests = request.session.get('current_guests'), booking_start_date_time = json.loads(request.session.get('current_start_datetime'), object_hook=DecodeDateTime), booking_end_date_time = json.loads(request.session.get('current_end_datetime'), object_hook=DecodeDateTime))
        

    return render(request, 'app/bookings_create_table.html', {'table_form' : table_form})

def booking_edit_view(request, *args, **kwargs):
    form = editBookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'app/bookings_edit.html', context)




class DateTimeEncoder(JSONEncoder):
    def default (self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()

def DecodeDateTime(date):
    date = datetime.fromisoformat(date)
    return date
