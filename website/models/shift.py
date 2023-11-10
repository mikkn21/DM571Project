from typing import List
from datetime import datetime
from .enum_group import GroupType
from .member import Member

class Shift:
    def __init__(self, id: int, _from: datetime, _to: datetime, booked_members: List['Member'], group: GroupType, is_super: bool, member_capacity: int):
        self.id: int = id
        self._from: datetime = _from
        self._to: datetime = _to
        self.booked_members: List[Member] = booked_members
        self.group: GroupType = group
        self.notes: str = ""
        self.is_super: bool = is_super
        self.member_capacity = member_capacity


