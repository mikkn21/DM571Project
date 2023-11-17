from django.test import TestCase
from ..models.custom_exception import *
from ..models.show import Show
from ..models.enum_show_type import ShowType
from ..models.enum_group import GroupType
from ..models.database import Database, Condition
from ..models.member import Member
from ..models.shift import Shift
from ..models.super import *
from ..models.shift_creator import ShiftCreator
from datetime import datetime, timedelta

class SuperTests(TestCase):
    def setUp(self):
        # Create a test database instance
        self.test_db = Database()
        self.shift_creator = ShiftCreator(self.test_db)
        # Dummy members
        alice = Super(name='Alice', password='alice123', db=self.test_db, super_groups=[GroupType.SALES], shift_creator=self.shift_creator)
        alice.groups.append(GroupType.SALES)
        self.test_db.insert('members', alice)
        self.test_db.insert('members', Super(name='Bob', password='bob123', db=self.test_db, super_groups=[], shift_creator=self.shift_creator))

        # Setup a Member instance for tests
        self.member = Super(name='John Doe', password='password123', db=self.test_db, super_groups=[], shift_creator=self.shift_creator)
        self.member.groups.append(GroupType.SALES)

        # Dummy shifts
        shift1 = Shift(self.test_db, start_date=datetime.now() + timedelta(days=8), end_date=datetime.now() + timedelta(days=8,hours=4), 
                       booked_members=[], group=GroupType.SALES, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift1)

        show1 = Show(title="Show1", show_type=ShowType.EVENT, start_date=datetime.now(), 
                 end_date=datetime.now() + timedelta(days=1), db=self.test_db)
        self.test_db.insert('shows', show1)

    def test_give_free_ticket_success(self):
        temp_member = self.test_db.get("members", [Condition("id", 2)])[0]
        temp_member.give_free_ticket(1)
        temp_member2 = self.test_db.get("members", [Condition("id", 1)])[0]
        self.assertEquals(1, temp_member2.obtain_free_tickets)
    
    def test_add_super_to_group_success(self):
        self.member.add_super_to_group(1, GroupType.PR)
        alice = self.test_db.get("members", [Condition("id", 1)])
        self.assertIn(GroupType.PR, alice.super_groups)
    
    def test_add_super_to_group_fail_already_in_group(self):
        with self.assertRaises(ValueError):
            self.add_super_to_group(1, GroupType.SALES)

