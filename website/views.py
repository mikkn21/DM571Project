from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

from .models import *

# Create your views here.
def index(request):
    context = {"arr": [1,2,3,4], "shift": Shift(1, datetime.now(), datetime.now(), [], enum_group.Group.PR, False)}
    return HttpResponse(render(request, "website/schedule.html", context))

def test(request):
    return HttpResponse("test")

def login_page(request):
    return HttpResponse(render(request, "website/login.html"))

