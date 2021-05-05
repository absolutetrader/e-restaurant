from django import forms
from django.conf import settings
from app.models.booking_model import Table, Booking
from django.forms import ValidationError
from datetime import datetime, timedelta




class InitialBookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = [
            'guests',
            'bookingStartDateTime',
            'bookingEndDateTime',
            'table'
        ]
    
    def clean_guests(self):
        data = self.cleaned_data['guests']
        if data < 1:
                raise ValidationError("A booking must be for at least one person")
        return data
    def clean_user(self):
        data = self.cleaned_data['user']
        for obj in Booking.objects.all():
            if obj.user == data:
                raise ValidationError("You already have an active booking")
        return data
    

class FinalBookingForm(forms.Form):  
    table = 0
    #table = forms.RadioSelect(choices = Table.objects.all())
    #def __init__(self, dynamic_field_names, *args, **kwargs):
        #super(FinalBookingForm, self).__init__(*args, **kwargs)
        #for field_name in dynamic_field_names:
            #self.fields[field_name] = forms.ChoiceField()


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
