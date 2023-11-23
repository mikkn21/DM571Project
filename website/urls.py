
from django.urls import path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout, name="logout"),
    path("about_supers/", views.about_supers, name="about_supers"),
    path("super/", views.super, name="super"),
    path("super/create_user/", views.create_user, name="create_user"),
    path("super/create_show/", views.create_show, name="create_show"),
    path("book-shift/", views.book_shift, name="book_shift"),
    path("cancel-shift/", views.cancel_shift, name="cancel_shift"),
    path("super/list_users/", views.list_users, name="list_users"),
]

