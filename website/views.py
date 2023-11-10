from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import *

# Create your views here.
def index(request):
    context = {"shifts_and_shows": [
        Shift(1, datetime.now(), datetime.now(), [], GroupType.PR, False, 2),
        Shift(2, datetime.now(), datetime.now(), [], GroupType.CLEANING, False, 1),
        Shift(3, datetime.now(), datetime.now(), [], GroupType.SALES, False, 3),
        Show("Barbie", ShowType.EVENT, datetime.now(), datetime.now(), 1),
        Shift(4, datetime.now(), datetime.now(), [], GroupType.TECHNICAL, False, 2),
        Show("Avengers", ShowType.EVENT, datetime.now(), datetime.now(), 2),
        Shift(5, datetime.now(), datetime.now(), [], GroupType.FACILITY_SERVICE, False, 1),
        Show("The Adventures of Slaub", ShowType.EVENT, datetime.now(), datetime.now(), 3),
    ]}
    return HttpResponse(render(request, "website/schedule.html", context))

def supers(request):
    return HttpResponse(render(request, "website/supers.html"))

def login_page(request):
    return HttpResponse(render(request, "website/login.html"))

