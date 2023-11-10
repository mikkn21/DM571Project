from typing import List, Dict, TypedDict
from .member import Member
from .show import Show
from .shift import Shift


class DatabaseObjects(TypedDict):
    members: List[Member]
    shifts: List[Shift]
    shows: List[Show]

class Database:
    def __init__(self):
        self._data: DatabaseObjects = {
            'members': [],
            'shifts': [],
            'shows': []
        }

    def insert(self, table: str, object):
        self._data[table].append(object)

    # deletes all entries where all conditions are met
    def delete(self, table: str, condition: Dict[str, any]):
        [self._data[table].remove(object) for object in self._data[table] if check_condition(object, condition)]

    # updates all entries where all conditions are met
    def update(self, table: str, condition: Dict[str, str], updated_values: Dict[str, any]):
        objects_to_update = [object for object in self._data[table] if check_condition(object, condition)]
        for object in objects_to_update:
            for k, v in updated_values.items():
                object.__dict__[k] = v

    # get / return all entries where all conditions are met
    def get(self, table: str, condition: Dict[str, any]):
        return [object for object in self._data[table] if check_condition(object, condition)]

# checks if a given object meets all the conditions
def check_condition(object, condition) -> bool:
    return all(object.__dict__[k] == v for k,v in condition.items())

