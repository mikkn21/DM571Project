from typing import List, Dict, TypedDict
from .member import Member
from .show import Show
from .shift import Shift


class DatabaseRecords(TypedDict):
    members: List[Member]
    shifts: List[Shift]
    shows: List[Show]

class Database:
    def __init__(self):
        self._data: DatabaseRecords = {
            'members': [],
            'shifts': [],
            'shows': []
        }

    def insert(self, table: str, record):
        self._data[table].append(record)

    def delete(self, table: str, condition: Dict[str, any]):
        [self._data[table].remove(record) for record in self._data[table] if check_condition(record, condition)]

    def update(self, table: str, condition: Dict[str, str], updated_values: Dict[str, any]):
        records_to_update = [record for record in self._data[table] if check_condition(record, condition)]
        for record in records_to_update:
            for k, v in updated_values.items():
                record.__dict__[k] = v

    def get(self, table: str, condition: Dict[str, any]):
        return [record for record in self._data[table] if check_condition(record, condition)]


def check_condition(record, condition) -> bool:
    return all(record.__dict__[k] == v for k,v in condition.items())

