from .shift_creator import ShiftCreator

class AutomaticScheduler(ShiftCreator):
    def __init__(self, shiftcreator: ShiftCreator):
        self.__shiftcreator = shiftcreator

    def fetch_shows_and_create_shifts():
        pass