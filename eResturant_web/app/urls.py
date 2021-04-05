from django.urls import path
from app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.home, name="hello_there"),
]

urlpatterns += staticfiles_urlpatterns()
