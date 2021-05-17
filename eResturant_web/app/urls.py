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
    path('booking/existing', booking.booking_existing_view, name="bookings/existing"),
    path('create', booking.booking_create_view, name='bookings/create'),
    path('create/table', booking.booking_create_table_view, name='bookings/create/table'),
    path('edit', booking.booking_edit_view, name='bookings/edit'),
    path('edit/fail', booking.booking_edit_fail_view, name='bookings/edit/fail'),
    path('delete/edit', booking.booking_delete_edit_view, name='bookings/delete/edit'),
    path('delete', booking.booking_delete_view, name='bookings/delete'),
    path('meal', mealOrdering.meal_order_view, name='mealOrder'),
<<<<<<< HEAD
    #path('profile', loginSignup.profile_view, name='profile'),
    #path('order', mealOrdering.make_order_view, name='mealOrder/order')
=======
    path('order', mealOrdering.make_order_view, name='mealOrder/order'),
    path('editorder', mealOrdering.edit_order_view, name = 'mealOrder/edit')
>>>>>>> origin/meal_ordering

]

urlpatterns += staticfiles_urlpatterns()
