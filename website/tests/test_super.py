from django.test import TestCase
from ..models.custom_exception import *
from ..models.show import Show
from ..models.enum_show_type import ShowType
from ..models.enum_group import GroupType
from ..models.database import Database, Condition
from ..models.member import Member
from ..models.shift import Shift
from datetime import datetime, timedelta

class MemberTests(TestCase):
    def setUp(self):
        # Create a test database instance
        self.test_db = Database()

        # Dummy members
        alice = Member(name='Alice', password='alice123', db=self.test_db)
        alice.groups.append(GroupType.SALES)
        self.test_db.insert('members', alice)
        self.test_db.insert('members', Member(name='Bob', password='bob123', db=self.test_db))

        # Setup a Member instance for tests
        self.member = Member(name='John Doe', password='password123', db=self.test_db)
        self.member.groups.append(GroupType.SALES)

        # Dummy shifts
        shift1 = Shift(self.test_db, start_date=datetime.now() + timedelta(days=8), end_date=datetime.now() + timedelta(days=8,hours=4), 
                       booked_members=[], group=GroupType.SALES, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift1)

        show1 = Show(title="Show1", show_type=ShowType.EVENT, start_date=datetime.now(), 
                 end_date=datetime.now() + timedelta(days=1), db=self.test_db)
        self.test_db.insert('shows', show1)

