from typing import List, TypedDict
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

    def insert(self, table, record):
        self._data[table].append(record)

    def query(self, table, conditions):
        # Implement a simple query logic
        return [record for record in self._data[table] if all(record[k] == v for k, v in conditions.items())]

    def update(self, table, conditions, update_values):
        # Implement update logic
        for record in self._data[table]:
            if all(record[k] == v for k, v in conditions.items()):
                for k, v in update_values.items():
                    record[k] = v

    def delete(self, table, conditions):
        # Implement delete logic
        self._data[table] = [record for record in self._data[table] if not all(record[k] == v for k, v in conditions.items())]