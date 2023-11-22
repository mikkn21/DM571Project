from typing import List, Dict, TypedDict


class Condition:
    """
    Represents a condition to be applied in database operations.

    Parameters:
    -----------
    key : str
        The key or attribute name to which the condition will be applied.
    value : any
        The value to be compared against the attribute specified by 'key'.
    compare : function, optional
        A function that defines how the comparison is made between the attribute's 
        value and the specified value. Default is lambda x,y: x == y (checks for equality).
    """
    def __init__(self, key: str, value, compare=lambda x,y: x==y):
        self.key = key
        self.value = value
        self.compare = compare

class ID:
    def __init__(self, key: str, value):
        self.key = key
        self.value = value


class DatabaseObjects(TypedDict):
    members: List["Member"]
    shifts: List["Shift"]
    shows: List["Show"]
    ids: List[ID]

class Database:
    def __init__(self):
        self._data: DatabaseObjects = {
            'members': [],
            'shifts': [],
            'shows': [],
            'ids': [ID("members", 0), ID("shifts", 0), ID("shows", 0)],
        }

    def insert(self, table: str, object, conditions: List[Condition] = []):
        """
        will only insert the given object, if there are no object in the database, that matches the condition(s)
        """
        if not conditions or not self.get(table, conditions):
            self._data[table].append(object)

    # deletes all entries where all conditions are met
    def delete(self, table: str, conditions: List[Condition]):
        [self._data[table].remove(object) for object in self._data[table] if check_condition(object, conditions)]

    # updates all entries where all conditions are met
    def update(self, table: str, conditions: List[Condition], updated_values: Dict[str, any]):
        objects_to_update = [object for object in self._data[table] if check_condition(object, conditions)]
        for object in objects_to_update:
            for k, v in updated_values.items():
                object.__dict__[k] = v

    # get / return all entries where all conditions are met
    def get(self, table: str, conditions: List[Condition]):
        return [object for object in self._data[table] if check_condition(object, conditions)]

# checks if a given object meets all the conditions
def check_condition(object, conditions) -> bool:
    return all(c.compare(object.__dict__[c.key], c.value) for c in conditions)

