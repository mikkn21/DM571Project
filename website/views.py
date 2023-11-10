from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import *

# Create your views here.
def index(request):
    context = {"shift_and_shows": [
        Shift(1, datetime.now(), datetime.now(), [], enum_group.Group.PR, False),
        Shift(2, datetime.now(), datetime.now(), [], enum_group.Group.CLEANING, False),
        Shift(3, datetime.now(), datetime.now(), [], enum_group.Group.SALES, False),
        Show("Barbie", ShowType.EVENT, datetime.now(), datetime.now(), 1),
        Shift(4, datetime.now(), datetime.now(), [], enum_group.Group.TECHNICAL, False),
        Show("Avengers", ShowType.EVENT, datetime.now(), datetime.now(), 2),
        Shift(5, datetime.now(), datetime.now(), [], enum_group.Group.FACILITY_SERVICE, False),
        Show("The Adventures of Slaub", ShowType.EVENT, datetime.now(), datetime.now(), 3),
    ]}
    return HttpResponse(render(request, "website/schedule.html", context))

def test(request):
    return HttpResponse("test")

def login_page(request):
    return HttpResponse(render(request, "website/login.html"))

