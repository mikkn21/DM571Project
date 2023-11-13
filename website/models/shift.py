from typing import List
from datetime import datetime
from .enum_group import GroupType
from .member import Member

class Shift:
    def __init__(self, id: int, start_date: datetime, end_date: datetime, booked_members: List['Member'], group: GroupType, is_super: bool, member_capacity: int):
        self.id: int = id
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date
        self.booked_members: List[Member] = booked_members
        self.group: GroupType = group
        self.notes: str = ""
        self.is_super: bool = is_super
        self.member_capacity = member_capacity


