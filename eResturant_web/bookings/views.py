from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookings_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>I'm meant to be a booking page</h1>")
    return render(request, 'bookings.html', {})