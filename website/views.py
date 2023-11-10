from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import *

# Create your views here.
def index(request):
    shifts_and_shows = [
        Shift(1, datetime.now(), datetime.now(), [], GroupType.PR, False, 2),
        Shift(2, datetime.now(), datetime.now(), [], GroupType.CLEANING, False, 1),
        Shift(3, datetime.now(), datetime.now(), [], GroupType.SALES, False, 3),
        Show("Barbie", ShowType.EVENT, datetime.now(), datetime.now(), 1),
        Shift(4, datetime.now(), datetime.now(), [], GroupType.TECHNICAL, False, 2),
        Show("Avengers", ShowType.EVENT, datetime.now(), datetime.now(), 2),
        Shift(5, datetime.now(), datetime.now(), [], GroupType.FACILITY_SERVICE, False, 3),
        Show("The Adventures of Slaub", ShowType.EVENT, datetime.now(), datetime.now(), 3),
    ]
    shifts_and_shows = [(isinstance(shift_or_show, Shift), shift_or_show) for shift_or_show in shifts_and_shows] # map list to (is_shift, shift_or_show)
    context = {"shifts_and_shows": shifts_and_shows}
    return HttpResponse(render(request, "website/schedule.html", context))

def supers(request):
    return HttpResponse(render(request, "website/supers.html"))

def login_page(request):
    return HttpResponse(render(request, "website/login.html"))

def test(request):
    return HttpResponse(render(request, "website/test.html"))

