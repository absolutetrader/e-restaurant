from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from app.models import MealOrder, Booking, Menu, Rewards
from django import forms
from app.forms.meal_forms import MealOrderForm
from django.contrib.auth.decorators import login_required
from datetime import datetime, timedelta
from django.utils import timezone
from .invoice import calculateCost, discount

# Create your views here.


@login_required
def meal_order_view(request):
    if Booking.objects.filter(user=request.user).count() == 0:
        return redirect('/create')

    current_booking = Booking.objects.get(user=request.user)
    MealOrders = MealOrder.objects.filter(booking=current_booking)

    list = []
    total = 0
    for orders in MealOrders:
        list.append(orders.order.name + "(" +
                    orders.order.category + ") : $" + str(orders.order.price))
        total = total + orders.order.price

    return render(request, 'app/meal_order.html', {'list': list,
                                                   'total': total})


@login_required
def edit_order_view(request):
    template = 'app/meal_order_edit.html'
    context = {}
    current_user = request.user

    if Booking.objects.filter(user=current_user):
        current_booking = Booking.objects.get(user=request.user)
    else:
        return redirect('/create')

    date = current_booking.bookingStartDateTime
    if date - timezone.now() > timedelta(days=1):
        MealOrders = MealOrder.objects.filter(booking=current_booking)
        MealOrders.delete()
    else:
        return redirect("/meal")

    return render(request, template, context)


@login_required
def make_order_view(request):

    form = MealOrderForm(request.POST or None)
    current_user = request.user

    if Booking.objects.filter(user=current_user).count() == 0:
        return redirect('/create')

    this_booking = Booking.objects.filter(user=current_user)
    if form.is_valid():
        f = form.save(commit=False)
        f.booking = this_booking.first()
        f.save()

    context = {'form': form}

    return render(request, 'app/order.html', context)
