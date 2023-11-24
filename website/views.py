from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from datetime import timedelta
from typing import Optional

from .authentication import require_login, require_super_login
from .models import *
from .models.database import *
from .models.password_protection import *

from website.dummy_database import create_dummy_database

# Create your views here.

db = create_dummy_database()

datetime_argument_format = "%y-%m-%d"
date_format = "%d/%m/%Y"

@require_login
def index(request, context, member):
    if request.method != "GET":
        return redirect(login_page)

    context["schedule-name"] = "Your Schedule"

    schedule_is_for_current_user = True
    member_id = request.GET.get("member-id")
    if member.is_super && member_id != None:
        members = db.get("members", [Condition("id", member_id, lambda x, y: str(x) == str(y))])
        if len(members) > 0:
            schedule_is_for_current_user = False
            super_member = member
            member = members[0]
            context["schedule-name"] = member.name + "'s Schedule"

    base_date = request.GET.get("date")
    if base_date != None:
        base_date = datetime.strptime(base_date, datetime_argument_format)
    else:
        base_date = datetime.now()

    start_date, end_date = get_week_datetimes(base_date)
    schedule: Schedule = member.get_full_schedule(start_date, end_date)

    shifts_and_shows = schedule.shifts + schedule.shows

    shifts_and_shows.sort(key=lambda shift_or_show: shift_or_show.start_date)

    last_shift_or_show = None;
    for shift_or_show in shifts_and_shows:
        if last_shift_or_show == None or last_shift_or_show.start_date.date() != shift_or_show.start_date.date():
            shift_or_show.new_date = shift_or_show.start_date.date().strftime("%d/%m/%Y")
        shift_or_show.start_date_hour_min = shift_or_show.start_date.strftime("%H:%M")
        shift_or_show.end_date_hour_min = shift_or_show.end_date.strftime("%H:%M")
        if isinstance(shift_or_show, Shift):
            shift_or_show.booked_members_count = len(shift_or_show.booked_members)
            shift_or_show.is_bookable = shift_is_bookable(member, shift_or_show, schedule_is_for_current_user)
            shift_or_show.is_cancellable = shift_is_cancellable(member, shift_or_show, schedule_is_for_current_user)
            shift_or_show.is_booked = shift_is_booked(member, shift_or_show)
        last_shift_or_show = shift_or_show

    shifts_and_shows = [(isinstance(shift_or_show, Shift), shift_or_show) for shift_or_show in shifts_and_shows] # map list to (is_shift, shift_or_show)
    context["shifts_and_shows"] = shifts_and_shows
    context["start_date"] = start_date.strftime(date_format)
    context["end_date"] = (end_date - timedelta(seconds=1)).strftime(date_format)
    context["next_date"] = (end_date + timedelta(days=1)).strftime(datetime_argument_format)
    context["previous_date"] = (start_date - timedelta(days=1)).strftime(datetime_argument_format)
    return HttpResponse(render(request, "website/schedule.html", context))

def get_week_datetimes(datetime_in_week: datetime):
    """
    For the given datetime_in_week, which can be any day in a any week, return the
    beginning of the monday at that week and the beginning of the monday at the next week.
    """
    in_week = datetime_in_week.date()
    start_date = in_week - timedelta(days = in_week.weekday())
    end_date = start_date + timedelta(days = 7)
    min_time = datetime.min.time()
    return datetime.combine(start_date, min_time), datetime.combine(end_date, min_time)

def shift_is_bookable(member: Member, shift: Shift, schedule_is_for_current_user: bool):
    if not schedule_is_for_current_user:
        return False

    if len(shift.booked_members) >= shift.member_capacity:
        return False

    if shift.group not in member.groups:
        return False 

    if shift_is_booked(member, shift):
        return False

    if shift_is_old(shift):
        return False

    return True

def shift_is_booked(member: Member, shift: Shift):
    return member.id in shift.booked_members

def shift_is_cancellable(member: Member, shift: Shift, schedule_is_for_current_user: bool):
    if not schedule_is_for_current_user && shift_is_booked(member, shift):
        return True

    if shift_is_old(shift):
        return False

    if shift_is_soon(shift):
        return False

    return shift_is_booked(member, shift)

def shift_is_old(shift: Shift):
    return shift.end_date < datetime.now()

def shift_is_soon(shift: Shift):
    return shift.start_date - datetime.now() < timedelta(days = 7)

@require_login
def about_supers(request, context, super):

    supers: List[Super] = db.get("members", [Condition( "is_super", True)])
    for super in supers:
        super.groups_str = [group.name for group in super.super_groups]
    context["supers"] = supers
    print(supers)
    return HttpResponse(render(request, "website/about_supers.html", context))

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        members = db.get("members", [Condition("email", username)])
        if len(members) == 0:
            return redirect(login_page)
        member = members[0]

        password_is_correct = check_password(password, member.password)

        if password_is_correct:
            request.session["member"] = {}
            request.session["member"]["id"] = member.id
            request.session["member"]["name"] = member.name
            request.session["member"]["is_super"] = member.is_super
            return redirect(index)

    return HttpResponse(render(request, "website/login.html"))

@require_super_login
def super(request, context, super):
    return HttpResponse(render(request, "website/super.html", context))

def logout(request):
    if "member" in request.session:
        del request.session["member"]

    return redirect(login_page)

@require_super_login
def create_user(request, context, super):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password = request.POST.get("password")
        phone_number = request.POST.get("phone_number")
        member = Member(name, password, db, email, phone_number)

        for group in GroupType:
            value = request.POST.get(group.name.lower())
            if value == "on":
                member.groups.add(group)

        db.insert("members", member)
    
    return HttpResponse(render(request, "website/create_user.html", context))




@require_super_login
def create_show(request, context, super):
    if request.method == "POST":
        format_date = "%Y-%m-%dT%H:%M"
        title = request.POST.get("title")
        show_type = request.POST.get("show-type")
        show_type = ShowType[show_type.upper()]
        print(f"{show_type} + {type(show_type)}")
        start_date = datetime.strptime(request.POST.get("start-datetime"), format_date )
        end_date = datetime.strptime(request.POST.get("end-datetime"), format_date )
        show = Show(db, title, show_type, start_date, end_date)
        db.insert("shows", show)
        
    return HttpResponse(render(request, "website/create_show.html", context))

@require_login
def book_shift(request, context, member: Member):
    if request.method == "GET":
        try:
            shift_id = int(request.GET.get("shift-id"))
        except ValueError:
            print("Shift id is not an int")
            return redirect(index)

        try:
            member.book_shift(shift_id)
        except (ExceedingCapacityException, InvalidGroupException, MissingAccessRightsException, OutdatedActionException) as e:
            print(e.message)

    return redirect(index)

@require_login
def cancel_shift(request, context, member: Member):
    if request.method == "GET":
        try:
            shift_id = int(request.GET.get("shift-id"))
        except ValueError:
            print("Shift id is not an int")
            return redirect(index)

        try:
            member.cancel_shift(shift_id)
        except (OutdatedActionException, ValueError) as e:
            print(e.message)

    return redirect(index)

def get_current_member(context):
    members: List[Member] = db.get("members", [Condition("id", context["member"]["id"])])
    if len(members) == 0:
        return None
    return members[0]

@require_super_login
def list_users(request, context, super: Member):
    members: List[Member] = super.db.get("members", [])
    for member in members:
        member.groups_str = [group.name for group in member.groups]
    context["members"] = members
    return HttpResponse(render(request, "website/list_users.html", context))

