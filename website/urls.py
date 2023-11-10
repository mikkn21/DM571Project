
from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("supers/", views.supers, name="supers"),
    path("test/", views.test, name="test"),
]

