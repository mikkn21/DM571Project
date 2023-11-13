from datetime import datetime
from typing import List
from .show import Show

class Schedule:
    def __init__(self, start_date: datetime, end_date: datetime, shows: List["Show"], shifts: List["Shift"]):
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date
        self.shows: List["Show"] = shows
        self.shifts: List["Shift"] = shifts
