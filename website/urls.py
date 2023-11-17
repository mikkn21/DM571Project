
from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout, name="logout"),
    path("about_supers/", views.about_supers, name="about_supers"),
    path("super/", views.super, name="super"),
    path("create_user/", views.create_user, name="create_user"),
    path("create_show/", views.create_show, name="create_show"),
    path("process_login/", views.process_login, name="process_login"),
]

