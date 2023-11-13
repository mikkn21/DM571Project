
from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("about_supers/", views.about_supers, name="about_supers"),
    path("super/", views.super, name="super"),
]

