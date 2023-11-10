

from ast import List


class ExceedingCapacityException(Exception):
    """Exception raised when capacity is exceeded"""

    def __init__(self, capacity: int, message: str="The shift is already fully booked"):
        self.capacity = capacity
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}. Capacity is {self.capacity}."


class InvalidGroupException(Exception):
    """Exception raised when someone was not part of the correct group, to perform that action"""

    def __init__(self, message="You are not part of the correct group"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
    
class MissingAccessRightsException(Exception):
    """Exception raised when someone tried to do an action, but did not have the access rights"""

    def __init__(self, message="You do not have the access right to perform this action"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"
    

class OutdatedActionException(Exception):
    """Exception raised when someone tried to do an action, but the action is outdated"""

    def __init__(self, message="The action you tried to do is not available anymore"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"