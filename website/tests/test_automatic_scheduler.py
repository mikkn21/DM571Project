from django.test import TestCase

from ..models.automatic_scheduler import AutomaticScheduler
from ..models.custom_exception import *
from ..models.show import Show
from ..models.enum_show_type import ShowType
from ..models.enum_group import GroupType
from ..models.database import Database, Condition
from ..models.member import Member
from ..models.shift import Shift
from unittest.mock import patch
from datetime import datetime, timedelta

class AutomaticSchedulerTests(TestCase):
    def setUp(self):
        self.test_db = Database()
        self.standard_groups: List[GroupType] = [GroupType.CLEANING, GroupType.SALES, GroupType.TECHNICAL]
        self.automatic_scheduler = AutomaticScheduler(self.test_db, self.standard_groups)


    @patch('website.models.automatic_scheduler.AutomaticScheduler._AutomaticScheduler__get_shows_from_API')
    def test_fetch_shows_and_create_shifts_success(self, mock_get_shows):
        mock_get_shows.return_value = [
            Show(self.test_db, "Barbie", ShowType.EVENT, datetime.now() + timedelta(days=20), datetime.now() + timedelta(days=20,hours=2.5)),
            Show(self.test_db, "Barbie", ShowType.EVENT, datetime.now() + timedelta(days=20), datetime.now() + timedelta(days=20,hours=2.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=24), datetime.now() + timedelta(days=24, hours=2.5)), 
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=21), datetime.now() + timedelta(days=21,hours=2.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=22), datetime.now() + timedelta(days=22,hours=2.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=23), datetime.now() + timedelta(days=23,hours=2.5)),
            Show(self.test_db, "Barbie", ShowType.PREMIERE, datetime.now() + timedelta(days=6, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=7, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=8, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=9, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.test_db, "Barbie", ShowType.MOVIE, datetime.now() + timedelta(days=10, hours=3), datetime.now() + timedelta(days=24,hours=5.5)),
            Show(self.test_db, "Oppenheimer", ShowType.PREMIERE, datetime.now() + timedelta(days=5), datetime.now() + timedelta(days=5,hours=2.5)),
            Show(self.test_db, "Oppenheimer", ShowType.EVENT, datetime.now() + timedelta(days=6), datetime.now() + timedelta(days=6,hours=2.5)),
            Show(self.test_db, "Oppenheimer", ShowType.MOVIE, datetime.now() + timedelta(days=7), datetime.now() + timedelta(days=7,hours=2.5)),
            Show(self.test_db, "Oppenheimer", ShowType.MOVIE, datetime.now() + timedelta(days=8), datetime.now() + timedelta(days=8,hours=2.5)),
            Show(self.test_db, "Oppenheimer", ShowType.MOVIE, datetime.now() + timedelta(days=9), datetime.now() + timedelta(days=9,hours=2.5)),
            Show(self.test_db, "Dune", ShowType.MOVIE, datetime.now() + timedelta(days=27), datetime.now() + timedelta(days=27,hours=3)),
            Show(self.test_db, "Dune", ShowType.MOVIE, datetime.now() + timedelta(days=24,hours=3), datetime.now() + timedelta(days=24,hours=6.5)),
            Show(self.test_db, "Dune", ShowType.MOVIE, datetime.now() + timedelta(days=19,hours=6.5), datetime.now() + timedelta(days=19,hours=9.5)),
            Show(self.test_db, "Wonka", ShowType.MOVIE, datetime.now() + timedelta(days=14), datetime.now() + timedelta(days=14,hours=2.5)),
            Show(self.test_db, "Wonka", ShowType.MOVIE, datetime.now() + timedelta(days=15,hours=3), datetime.now() + timedelta(days=15,hours=5.5)),
            Show(self.test_db, "Wonka", ShowType.MOVIE, datetime.now() + timedelta(days=16,hours=6), datetime.now() + timedelta(days=16,hours=8.5)),
            Show(self.test_db, "007 Skyfall", ShowType.PREMIERE, datetime.now() - timedelta(days=20,hours=6), datetime.now() + timedelta(days=20,hours=8.5)),
            Show(self.test_db, "007 Skyfall", ShowType.MOVIE, datetime.now() - timedelta(days=19,hours=6), datetime.now() - timedelta(days=19,hours=3.5)),
            Show(self.test_db, "007 Skyfall", ShowType.MOVIE, datetime.now() - timedelta(days=18,hours=6), datetime.now() - timedelta(days=18,hours=3.5)),
            Show(self.test_db, "007 Skyfall", ShowType.MOVIE, datetime.now() - timedelta(days=17,hours=6), datetime.now() - timedelta(days=17,hours=3.5)),
        ]

        self.automatic_scheduler.fetch_shows_and_create_shifts()
        self.assertEqual((len(mock_get_shows.return_value)-1)*len(self.standard_groups), len(self.test_db.get("shifts", []))) # -1 since there are one duplicate entry in shows
