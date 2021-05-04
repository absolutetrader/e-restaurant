from django.shortcuts import render
from django.http import HttpResponse
from app.models import Booking, userProfile, Table
from app.forms import InitialBookingForm, editBookingForm, FinalBookingForm
from django.shortcuts import redirect

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
            #final_form = FinalBookingForm(get_available_tables(initial_form.cleaned_data.get("bookingStartDateTime"), initial_form.cleaned_data.get("bookingEndDateTime"), initial_form.cleaned_data.get("guests")))    
            
            
      
    return render(request, 'app/bookings_create.html', { 'initial_form' : initial_form})

    

def booking_edit_view(request, *args, **kwargs):
    form = editBookingForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookingForm()
    context = {
        'form': form
    }
    return render(request, 'app/bookings_edit.html', context)



def get_available_tables(booking_start_date_time, booking_end_date_time, guests):
    l_bound_time = booking_start_date_time
    u_bound_time = booking_end_date_time

    tables_booked_ids = []
    # Exclude tables which start and end booking date includes requested initial booking date_time
    tables_booked = Booking.objects.filter(bookingStartDateTime__lt= l_bound_time, bookingEndDateTime__gt = l_bound_time).values('table')
    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which start and end booking date includes requested ending booking date_time
    tables_booked = Booking.objects.filter(bookingStartDateTime__lt = u_bound_time, bookingEndDateTime__gt = u_bound_time).values('table')
    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which booking slots is inside requested booking slot
    tables_booked = Booking.objects.filter(bookingStartDateTime__gt = l_bound_time, bookingEndDateTime__lt = u_bound_time).values('table')
    tables_booked_ids_temp = [x['table'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Exclude tables which include requested booking slot
    tables_booked = Booking.objects.filter(bookingStartDateTime__lt = l_bound_time, bookingEndDateTime__gt = u_bound_time).values('table')
    tables_booked_ids_temp = [x['tablee'] for x in tables_booked]
    tables_booked_ids = tables_booked_ids + tables_booked_ids_temp

    # Then I get a list of all the tables, of the needed size, available in that restaurant and
    # I exclude the previous list of unavailable tables. I order the list from the smaller table
    # to the bigger one and I return the first, smaller one, available.
    tables = Table.objects.filter(maxCapacity__gte=guests).exclude(id__in=tables_booked_ids)

    return tables