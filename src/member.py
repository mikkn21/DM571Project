from typing import Optional
from typing import List, Dict
from datetime import datetime
from enum_group import Group

class Member:
    def __init__(self, name: str):
        self.id: int = self.create_id()
        self.name: str = name
        self.hiring_date: datetime = datetime.now()
        self.obtained_free_tickets: int = 0
        self.groups: List[Group] = []
        self.shifts_completed: Dict[int] = {group: 0 for group in Group}


    def get_free_tickets_remaining_count(self) -> int:
        return self.obtained_free_tickets
    
    def create_id(self):
        pass


    def book_shift(self, shift: Shift):
        pass

    def cancel_shift(self, shift: Shift) -> bool:
        pass
    
    def get_full_schedule(self, _from: datetime, to: datetime) -> Schedule:
        pass

    def get_own_schedule(self, _from: datetime, to: datetime)  -> Schedule:
        pass   


