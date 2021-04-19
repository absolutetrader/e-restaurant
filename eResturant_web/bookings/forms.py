from django import forms
from .models import Booking
from django.forms import ValidationError
from tempus_dominus.widgets import DatePicker, TimePicker, DateTimePicker


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'table',
            'guests',
            'bookingStartDateTime',
            'bookingEndDateTime'
        ]
        widgets = {
            'table': forms.RadioSelect(),
        }

    def clean_guests(self):
        guests = self.cleaned_data['guests']

        if guests < 1:
            raise ValidationError('Booking must be for 1 or more people')
        return guests
    
    def clean(self):
        super(BookingForm, self).clean()  
        guests = self.cleaned_data.get('guests')
        max_guests = self.cleaned_data.get('table').maxCapacity

        if guests > max_guests:
            raise ValidationError('Booking has exceeded the capacity of the table')
    
    

        

class editBookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'id',
            'guests',
            'table',
            'bookingStartDateTime',
            'bookingEndDateTime'
        ]
