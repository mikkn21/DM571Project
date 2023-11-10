from typing import List, Dict
from datetime import datetime
from .password_protection import hash_password
from .enum_group import GroupType
from .schedule import Schedule


class Member:
    def __init__(self, name: str, password: str):
        self.id: int = self.create_id()
        self.name: str = name
        self.password: any = hash_password(password)
        self.hiring_date: datetime = datetime.now()
        self.obtained_free_tickets: int = 0
        self.groups: List[GroupType] = []
        self.shifts_completed: Dict[int] = {group_type: 0 for group_type in GroupType}
        self.next_id: int = 0


    def get_free_tickets_remaining_count(self) -> int:
        return self.obtained_free_tickets
    
    # id 0 is reserved for admin
    def create_id(self):
        self.next_id += 1
        return self.next_id

    def book_shift(self, shift: "Shift"):
        pass

    def cancel_shift(self, shift: "Shift") -> bool:
        pass
    
    def get_full_schedule(self, _from: datetime, to: datetime) -> Schedule:
        pass

    def get_own_schedule(self, _from: datetime, to: datetime)  -> Schedule:
        pass
