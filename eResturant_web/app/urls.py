from django.urls import path, include
from app.views import booking, loginSignup, mealOrdering
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", loginSignup.home, name="home"),
    path("hello/<name>", loginSignup.hello_there, name="hello_there"),
    path("register", loginSignup.register, name="register"),
    path("login", loginSignup.login_view, name="login"),
    path('logout', loginSignup.logout_view, name='logout'),
    path('booking', booking.bookings_view, name='bookings'),
    path('create', booking.booking_create_view, name='bookings/create'),
    path('create/table', booking.booking_create_table_view, name='bookings/create/table'),
    path('edit', booking.booking_edit_view, name='bookings/edit'),
    path('meal', mealOrdering.meal_order_view, name='mealOrder'),
    #path('order', mealOrdering.make_order_view, name='mealOrder/order')

]

urlpatterns += staticfiles_urlpatterns()
