from django.shortcuts import render
from .forms import MealOrderForm

# Create your views here.
def mealOrder_view(request):
    context = {}
    return render(request, 'home.html', context)

def make_order_view(request):
    form = MealOrderForm()
    context = {'form':form}
    return render(request, 'order.html', context)