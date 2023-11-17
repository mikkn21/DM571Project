from typing import List, Dict
from datetime import datetime
from datetime import timedelta
from .password_protection import hash_password
from .enum_group import GroupType
from .schedule import Schedule
from .custom_exception import *
from .database import Condition, Database

class Member:
    def __init__(self, name: str, password: str, db: Database):
        self.db = db
        self.id: int = self.__create_id()
        self.name: str = name
        self.password: any = hash_password(password)
        self.hiring_date: datetime = datetime.now()
        self.obtained_free_tickets: int = 0
        self.groups: List[GroupType] = []
        self.shifts_completed: Dict[int] = {group_type: 0 for group_type in GroupType}
        self.is_super = False


    def get_free_tickets_remaining_count(self) -> int:
        return self.obtained_free_tickets
    
    # id 0 is reserved for admin
    # should be locked while modifying database
    def __create_id(self):
        ids = self.db.get("ids", [Condition("key", "members")])
        if len(ids) != 1:
            raise ValueError("invalid amount of ids for show in database")
        new_id = ids[0].value+1
        self.db.update("ids", [Condition("key", "members")], {"value": new_id})
        return new_id
    
    def __get_element_by_id(self, table: str, id: int) -> "Shift":
        element = self.db.get(table, [Condition("id", id)])
        if len(element) != 1:
            raise ValueError("invalid id")
        return element[0]

    # should be locked while modifying database
    def book_shift(self, shift_id: int):
        shift: "Shift" = self.__get_element_by_id("shifts", shift_id)
        if len(shift.booked_members) >= shift.member_capacity:
            raise ExceedingCapacityException("Max capacity of members already reached, booking denied")
        elif shift.group not in self.groups: 
            raise InvalidGroupException("Member attempted to book a shift for a group they are not a part of")
        elif shift.is_super != False:
            raise MissingAccessRightsException("Member attempted to book a shift meant for a super")
        elif shift.end_date < datetime.now():
            raise OutdatedActionException("Member attempted to book a shift that is too old")
        else: 
            shift.booked_members.append(self.id)
            self.db.update("shifts", [Condition("id", shift.id)], {"booked_members": shift.booked_members})

    # should be locked while modifying database
    def cancel_shift(self, shift_id: int):
        shift: "Shift" = self.__get_element_by_id("shifts", shift_id)
        if shift.end_date < datetime.now() + timedelta(days=7):
            raise OutdatedActionException("Member attempted to cancel a shift that is either too old or within a week")
        elif self.id not in shift.booked_members:
            raise ValueError("Member cannot cancel a shift, that they have not booked")
        else:
            shift.booked_members.remove(self.id)
            self.db.update("shifts", [Condition("id", shift.id)], {"booked_members": shift.booked_members})
    
    def get_full_schedule(self, start_date: datetime, end_date: datetime) -> Schedule:
        if start_date > end_date:
            raise ValueError("Invalid date times")
        shifts: List["Shift"] = self.db.get("shifts", [Condition("start_date", start_date, lambda x, y: x > y), Condition("end_date", end_date, lambda x, y: x < y)])
        shows: List["Show"] = self.db.get("shows", [Condition("start_date", start_date, lambda x, y: x > y), Condition("end_date", end_date, lambda x, y: x < y)])
        return Schedule(start_date, end_date, shows, shifts)
    
    def get_own_schedule(self, start_date: datetime, end_date: datetime)  -> Schedule:
        if start_date > end_date:
            raise ValueError("Invalid date times")
        groups_condition = [Condition("group", group_type, lambda x,y: x!=y) for group_type in GroupType if group_type not in self.groups]
        conditions = [Condition("start_date", start_date, lambda x, y: x > y), Condition("end_date", end_date, lambda x, y: x < y)]
        conditions.extend(groups_condition)
        shifts: List["Shift"] = self.db.get("shifts", conditions)
        shows: List["Show"] = self.db.get("shows", [Condition("start_date", start_date, lambda x, y: x > y), Condition("end_date", end_date, lambda x, y: x < y)])
        return Schedule(start_date, end_date, shows, shifts)
