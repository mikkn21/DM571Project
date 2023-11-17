from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .session_user import SessionMember
from .authentication import require_login, require_super_login

from .models import *

# Create your views here.

@require_login
def index(request, context):
    shifts_and_shows = [
        Shift(1, datetime.now(), datetime.now(), [], GroupType.PR, False, 2),
        Shift(2, datetime.now(), datetime.now(), [], GroupType.CLEANING, False, 1),
        Shift(3, datetime.now(), datetime.now(), [], GroupType.SALES, False, 3),
        Show("Barbie", ShowType.EVENT, datetime.now(), datetime.now(), 1),
        Shift(4, datetime(2023, 8, 13, 6, 14, 47), datetime(2023, 8, 13, 10, 17, 47), [], GroupType.TECHNICAL, False, 2),
        Show("Avengers", ShowType.EVENT, datetime.now(), datetime.now(), 2),
        Shift(5, datetime.now(), datetime.now(), [], GroupType.FACILITY_SERVICE, False, 3),
        Show("The Adventures of Slaub", ShowType.EVENT, datetime.now(), datetime.now(), 3),
    ]

    shifts_and_shows.sort(key=lambda shift_or_show: shift_or_show.start_date)

    last_shift_or_show = None;
    for shift_or_show in shifts_and_shows:
        if last_shift_or_show == None or last_shift_or_show.start_date.date() != shift_or_show.start_date.date():
            shift_or_show.new_date = shift_or_show.start_date.date().strftime("%d/%m/%Y")
        shift_or_show.start_date_hour_min = shift_or_show.start_date.strftime("%H:%M")
        shift_or_show.end_date_hour_min = shift_or_show.end_date.strftime("%H:%M")
        if isinstance(shift_or_show, Shift):
            shift_or_show.booked_members_count = len(shift_or_show.booked_members)
            shift_or_show.is_bookable = True
            shift_or_show.is_cancellable = False
        last_shift_or_show = shift_or_show

    print(request.session["member"])
    shifts_and_shows = [(isinstance(shift_or_show, Shift), shift_or_show) for shift_or_show in shifts_and_shows] # map list to (is_shift, shift_or_show)
    context["shifts_and_shows"] = shifts_and_shows
    return HttpResponse(render(request, "website/schedule.html", context))

@require_login
def about_supers(request, context):
    return HttpResponse(render(request, "website/about_supers.html", context))

def login_page(request):
    return HttpResponse(render(request, "website/login.html"))

@require_super_login
def super(request, context):
    return HttpResponse(render(request, "website/super.html", context))

def process_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the username and password are 'admin'
        if username == 'admin' and password == 'admin':
            request.session["member"] = {}
            request.session["member"]["id"] = 2
            request.session["member"]["name"] = "John Doe"
            request.session["member"]["is_super"] = True
            return redirect(index)
        else:
            request.session["member"] = {}
            request.session["member"]["id"] = 2
            request.session["member"]["name"] = "John Doe"
            request.session["member"]["is_super"] = False
            return redirect(index)

    # Handle GET requests or other cases
    return render(request, 'website/login.html')

def logout(request):
    if "member" in request.session:
        del request.session["member"]

    return redirect(login_page)

@require_super_login
def create_user(request, context):
    return HttpResponse(render(request, "website/create_user.html", context))

@require_super_login
def create_show(request, context):
    return HttpResponse(render(request, "website/create_show.html", context))

