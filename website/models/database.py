from typing import List, Dict, TypedDict
from member import Member
from show import Show
from shift import Shift


class DatabaseRecords(TypedDict):
    members: List[Member]
    shifts: List[Shift]
    shows: List[Show]





class MockDatabase:
    def __init__(self):
        self._data: DatabaseRecords = {
            'members': [],
            'shifts': [],
            'shows': []
        }

    def insert(self, table: str, record):
        self._data[table].append(record)

    def delete(self, table: str, condition: Dict[str, any]):
        [self._data[table].remove(record) for record in self._data[table] if all(record.__dict__[k] == v for k,v in condition.items())]

    def update(self, table: str, condition: Dict[str, str], updated_values: Dict[str, str]):
        [n for n, record in self._data[table]]

