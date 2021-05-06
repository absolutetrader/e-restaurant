from django.shortcuts import render
from django.http import HttpResponse
from app.models import MealOrder, Booking
from django import forms
from app.forms.meal_forms import MealOrderForm

# Create your views here.


def meal_order_view(request):
    context = {}
    return render(request, 'app/meal_order.html', context)


def make_order_view(request):   

    form = MealOrderForm(request.POST or None)
    current_user = request.user
    this_booking = Booking.objects.filter(user = current_user)
    if form.is_valid():
        f = form.save(commit=False)
        f.booking = this_booking.first()
        f.save()
    
    context = {'form': form}

    return render(request, 'app/order.html', context)
