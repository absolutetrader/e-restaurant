from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.utils.timezone import datetime
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ProfileForm


# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    return render(
        request,
        'app/hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )


def register(request):
    if request.method == "POST":
        u_form = NewUserForm(request.POST)
        p_form = ProfileForm(request.POST)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(
                request, f'Registration complete! You may log in!')
            return redirect('home')
    else:
        u_form = NewUserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'app/register.html', {'u_form': u_form, 'p_form': p_form})
