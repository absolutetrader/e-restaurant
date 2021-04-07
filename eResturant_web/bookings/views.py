from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bookings_view(request, *args, **kwargs):
    my_context = {
        "my_text":  "This is about us",
        "my_number": 123,
        "my_list": [123, 424, 12321]
    }
    return render(request, 'bookings.html', my_context)