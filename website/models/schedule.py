from datetime import datetime
from typing import List
from .show import ShowType

class Schedule:
    def __init__(self, _from: datetime, _to: datetime, shows: List[ShowType], shifts: List["Shift"]):
        self._from: datetime = _from
        self._to: datetime = _to
        self.shows: List[ShowType] = shows
        self.shifts: List["Shift"] = shifts
