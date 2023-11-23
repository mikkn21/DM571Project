
from datetime import datetime
from datetime import timedelta
from .models import *

from itertools import combinations

def create_dummy_database():
    db = Database()

    members = __get_members(db)
    for member in members:
        db.insert("members", member)
    admin = Super("Admin", "admin", db, "admin@gmail.com", "+232323432", [GroupType.CLEANING, GroupType.SALES], ShiftCreator(db))
    admin.is_super = True
    db.insert("members", admin)

    shifts = __get_shifts(db, members)
    shift_creator = ShiftCreator(db)
    for shift in shifts:
        shift_creator.create_shift(shift)

    shows = __get_shows(db)
    for show in shows:
        db.insert("shows", show)

    return db

def __get_members(db: Database):
    members = []
    for n, group in enumerate(GroupType):
        name = group.name.lower()
        member = Member(name, name, db, f"{name}@gmail.com", f"+45{str(n)*8}")
        member.groups.add(group)
        members.append(member)
    return members

def __get_shifts(db: Database, members):
    now = datetime.now()
    shifts = []
    i = 0
    for day in range(0, 14, 2):
        for hour in range(0, 20, 10):
            start = now + timedelta(days = day, hours = hour)
            start = start - timedelta(minutes = start.minute)
            duration = timedelta(hours = 4)
            group = GroupType((i % len(GroupType)) + 1)
            shift = Shift(db, start, start + duration, [], group, False, 1)
            shifts.append(shift)
            i += 1
    return shifts

def __get_shows(db: Database):
    now = datetime.now()
    shows = []
    i = 0
    for day in range(7):
        for hour in range(0, 20, 10):
            start = now + timedelta(days = day, hours = hour)
            start = start - timedelta(minutes = start.minute)
            duration = timedelta(hours = 4)
            show_type = ShowType((i % len(ShowType)) + 1)
            show = Show(db, "Barbie", show_type, start, start + duration)
            shows.append(show)
            i += 1
    return shows

