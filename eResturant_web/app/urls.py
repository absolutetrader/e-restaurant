from django.urls import path, include
from app import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.home, name="home"),

    path("hello/<name>", views.hello_there, name="hello_there"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path('logout', views.logout_view, name='logout')


]

urlpatterns += staticfiles_urlpatterns()
