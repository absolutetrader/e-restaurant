from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.utils.timezone import datetime
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserForm, ProfileForm
from django.contrib.auth import login, logout


# Create your views here.
def home(request):
    current_user = request.user

    return render(request, 'app/home.html')


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
        u_form = NewUserForm(request.POST or None)
        p_form = ProfileForm(request.POST or None)
        if u_form.is_valid() and p_form.is_valid():
            user = u_form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            login(request, user)
            messages.success(
                request, f'Registration complete!')
            return redirect('home')
    else:
        u_form = NewUserForm(request.POST)
        p_form = ProfileForm(request.POST)
    return render(request, 'app/register.html', {'u_form': u_form, 'p_form': p_form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            user = form.get_user()
            login(request, user)
            return redirect('/')

    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})

# logout view


def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('/')
