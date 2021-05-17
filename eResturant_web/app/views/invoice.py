from threading import Condition, current_thread
from django.db import models
from django.http import request
from django.shortcuts import render, get_object_or_404, redirect

from app.models.meal_model import MealOrder
from app.models.booking_model import Booking
from app.models.invoice_model import InVoice
from app.forms.invoice_forms import InvoiceForm
from app.models.user_model import userProfile
from app.models.rewards_model import Rewards


def calculateCost(bookingID, userC):
    cost = 0
    for price in MealOrder.objects.all().filter(Booking_id=bookingID):
        cost += price.order.price

    return cost - cost * discount(userC)


def discount(userC):
    userP = userProfile.objects.get(user=userC)
    reward = Rewards.objects.get(id=1)
    if userP.visits > reward.condition and userP.visits % reward.condition == 0:
        return reward.discount
    else:
        return 0


def get_invoice(request, *args, **kwargs):
    form = InvoiceForm(request.POST or None)
    #paid_form = PaidForm(request.POST or None)

    if form.is_valid():
        saved = form.save(commit=False)

        bookingID = form.cleaned_data['booking']
        tableNo = Booking.objects.all().filter(id=bookingID.id)
        userC = request.user
        saved.price = calculateCost(bookingID, userC)
        price = saved.price
        discountU = discount(userC) * 100
        order = MealOrder.objects.all().filter(Booking_id=bookingID)
        paid = request.GET.get('y')
        saved.save()

        if paid:
            intance = Booking.objects.get(id=bookingID.id)
            intance.delete()
            return redirect('/invoice')
        # reward()

        args = {
            'form': form,
            'price': price,
            'order': order,
            'tableNo': tableNo,
            'discount': discountU,
        }

    else:
        args = {
            'form': form,
        }

    return render(request, 'app/invoice.html', args)
