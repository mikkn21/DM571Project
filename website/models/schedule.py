from datetime import datetime
from typing import List
from .shift import Shift
from .show import Show

class Schedule:
    def __init__(self, _from: datetime, _to: datetime, shows: List[Show], shifts: List[Shift]):
        self._from: datetime = _from
        self._to: datetime = _to
        self.shows: List[Show] = shows
        self.shifts: List[Shift] = shifts
