from django.shortcuts import render
from django.http import HttpResponse
from app.models import MealOrder, Booking, Menu
from django import forms
from app.forms.meal_forms import MealOrderForm

# Create your views here.


def meal_order_view(request):
    current_booking = Booking.objects.get(user = request.user)
    MealOrders = MealOrder.objects.filter(booking = current_booking)
    list = []
    
    for orders in MealOrders:
        list.append(orders.order.name + "(" + orders.order.category + ") : $" + str(orders.order.price))

    return render(request, 'app/meal_order.html', {'list' : list})


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
