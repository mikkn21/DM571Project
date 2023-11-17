from typing import List
from datetime import datetime
from ..models.database import Condition, Database
from .enum_group import GroupType
from .member import Member

class Shift:
    def __init__(self, db: Database, start_date: datetime, end_date: datetime, booked_members: List[int], group: GroupType, is_super: bool, member_capacity: int):
        self.db = db
        self.id: int = self.__create_id()
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date
        self.booked_members: List[int] = booked_members
        self.group: GroupType = group
        self.notes: str = ""
        self.is_super: bool = is_super
        self.member_capacity = member_capacity

    def __create_id(self):
        ids = self.db.get("ids", [Condition("key", "shifts")])
        if len(ids) != 1:
            raise ValueError("invalid amount of ids for shifts in database")
        new_id = ids[0].value+1
        self.db.update("ids", [Condition("key", "shifts")], {"value": new_id})
        return new_id
