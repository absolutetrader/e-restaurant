from django.shortcuts import render
from django.http import HttpResponse
#from app.models import MealOrder
#from app.forms import MealOrderForm

# Create your views here.


def meal_order_view(request):
    context = {}
    return render(request, 'app/meal_order.html', context)


"""def make_order_view(request):

    form_class = MealOrderForm
    form = form_class(request.POST or None)

    context = {'form': form}

    return render(request, 'app/order.html', context)"""
