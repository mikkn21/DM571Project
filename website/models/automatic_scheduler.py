from ast import List

from ..models.database import Database
from ..models.show import Show
from ..models.enum_show_type import ShowType
from .shift_creator import ShiftCreator
from datetime import datetime, timedelta

class AutomaticScheduler(ShiftCreator):
    def __init__(self, shiftcreator: ShiftCreator, db: Database):
        self.__shiftcreator = shiftcreator
        self.db = db

    def __get_shows_from_API(self):
        return [
            Show(self.db, "Barbie", ShowType.EVENT, datetime.now() + timedelta(days=20), datetime.now() + timedelta(days=20,hours=2.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=24), datetime.now() + timedelta(days=24, hours=2.5)), 
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=21), datetime.now() + timedelta(days=21,hours=2.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=22), datetime.now() + timedelta(days=22,hours=2.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=23), datetime.now() + timedelta(days=23,hours=2.5)),
            Show(self.db, "Barbie", ShowType.PREMIERE, datetime.now() + timedelta(days=6, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=7, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=8, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=9, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=10, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.db, "Oppenheimer", ShowType.PREMIERE, datetime.now() + timedelta(days=5), datetime.now() + timedelta(days=5,hours=2.5)),
            Show(self.db, "Oppenheimer", ShowType.EVENT, datetime.now() + timedelta(days=6), datetime.now() + timedelta(days=6,hours=2.5)),
            Show(self.db, "Oppenheimer", ShowType.MOVIE, datetime.now() + timedelta(days=7), datetime.now() + timedelta(days=7,hours=2.5)),
            Show(self.db, "Oppenheimer", ShowType.MOVIE, datetime.now() + timedelta(days=8), datetime.now() + timedelta(days=8,hours=2.5)),
            Show(self.db, "Oppenheimer", ShowType.MOVIE, datetime.now() + timedelta(days=9), datetime.now() + timedelta(days=9,hours=2.5)),
            Show(self.db, "Dune", ShowType.MOVIE, datetime.now() + timedelta(days=27), datetime.now() + timedelta(days=27,hours=3)),
            Show(self.db, "Dune", ShowType.MOVIE, datetime.now() + timedelta(days=24,hours=3), datetime.now() + timedelta(days=24,hours=6.5)),
            Show(self.db, "Dune", ShowType.MOVIE, datetime.now() + timedelta(days=19,hours=6.5), datetime.now() + timedelta(days=19,hours=9.5)),
            Show(self.db, "Wonka", ShowType.MOVIE, datetime.now() + timedelta(days=14), datetime.now() + timedelta(days=14,hours=2.5)),
            Show(self.db, "Wonka", ShowType.MOVIE, datetime.now() + timedelta(days=15,hours=3), datetime.now() + timedelta(days=15,hours=5.5)),
            Show(self.db, "Wonka", ShowType.MOVIE, datetime.now() + timedelta(days=16,hours=6), datetime.now() + timedelta(days=16,hours=8.5)),
            Show(self.db, "007 Skyfall", ShowType.PREMIERE, datetime.now() - timedelta(days=20,hours=6), datetime.now() + timedelta(days=20,hours=8.5)),
            Show(self.db, "007 Skyfall", ShowType.MOVIE, datetime.now() - timedelta(days=19,hours=6), datetime.now() - timedelta(days=19,hours=3.5)),
            Show(self.db, "007 Skyfall", ShowType.MOVIE, datetime.now() - timedelta(days=18,hours=6), datetime.now() - timedelta(days=18,hours=3.5)),
            Show(self.db, "007 Skyfall", ShowType.MOVIE, datetime.now() - timedelta(days=17,hours=6), datetime.now() - timedelta(days=17,hours=3.5)),
        ]

    def fetch_shows_and_create_shifts():
        shows = self.__get_shows_from_API()