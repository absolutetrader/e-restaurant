"""web_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from app.views import loginSignup, booking, mealOrdering


urlpatterns = [

    path("", include("app.urls")),
    path('admin/', admin.site.urls),


]

"""path('bookings/', bookings_view),
    path('bookings/create', booking_create_view),
    path('bookings/edit', booking_edit_view),
    path('mealorder/', mealOrder_view),
    path('mealorder/create', make_order_view)"""

"""path("hello/<name>", loginSignup.hello_there, name="hello_there"),
    path("register", loginSignup.register, name="register"),
    path("login", loginSignup.login_view, name="login"),
    path('logout', loginSignup.logout_view, name='logout'),
    path('bookings', booking.bookings_view, name='bookings'),
    path('bookings/create', booking.booking_create_view, name='bookings/create'),
    path('bookings/edit', booking.booking_edit_view, name='bookings/edit'),
    path('meal_order', mealOrdering.meal_order_view, name='mealOrder'),
    path('meal_order/order', mealOrdering.make_order_view, name='mealOrder/order')"""
