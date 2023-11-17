from .shift import Shift
from .database import Database

class ShiftCreator:
    def __init__(self, database: Database):
        self.db: Database = database

    def create_shift(self, shift: Shift):
        self.db.insert("shifts", shift)