from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
from .models import userProfile, Booking, MealOrder
from django.forms import ValidationError


class NewUserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = userProfile
        fields = ['First Name', 'Last Name']


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
        max_guests = self.cleaned_data.get('table').maxCapacity
        if guests is not None:
            if guests > max_guests:
                raise ValidationError(
                    'Booking has exceeded the capacity of the table')
            if guests < 1:
                raise ValidationError('Booking must be for 1 or more people')
        return guests

    def clean(self):
        super(BookingForm, self).clean()
        # if len(Booking.objects.all()) > 0:
        #raise ValidationError('You already have an active booking')
        for bookings in Booking.objects.filter(table=self.cleaned_data['table']):
            if(self.cleaned_data['bookingStartDateTime'] >= bookings.bookingStartDateTime and self.cleaned_data['bookingStartDateTime'] <= bookings.bookingEndDateTime):
                raise ValidationError(
                    "This table has already been booked for this time")


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


class MealOrderForm(forms.ModelForm):
    class Meta:
        model = MealOrder
        fields = '__all__'
