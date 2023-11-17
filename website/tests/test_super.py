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
from ..models.custom_exception import *
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
        super1 = self.test_db.get("members", [Condition("id", 1)])[0]
        super2 = self.test_db.get("members", [Condition("id", 2)])[0]
        super2.give_free_ticket(1)
        self.assertEquals(1, super1.obtained_free_tickets)
    
    def test_create_shift_success(self):
        shift = Shift(self.test_db, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 2)
        self.member.create_shift(shift)
        self.assertEquals(shift.id, self.test_db.get("shifts", [Condition("id", shift.id)])[0].id)

    def test_add_super_to_group_success(self):
        self.member.add_super_to_group(1, GroupType.PR)
        alice = self.test_db.get("members", [Condition("id", 1)])[0]
        self.assertIn(GroupType.PR, alice.super_groups)
    
    def test_add_super_to_group_fail_already_in_group(self):
        with self.assertRaises(ValueError):
            self.member.add_super_to_group(1, GroupType.SALES)

    def test_promote_to_super_success(self):
        member1 = Member(name='Troels', password='troels123', db=self.test_db)
        member1.groups.append(GroupType.SALES)
        self.test_db.insert('members', member1)
        self.member.promote_to_super(member1.id, [GroupType.SALES])
    
    def test_promote_to_super_fail_no_group(self):
        member1 = Member(name='Troels', password='troels123', db=self.test_db)
        member1.groups.append(GroupType.SALES)
        self.test_db.insert('members', member1)
        with self.assertRaises(InvalidGroupException):
            self.member.promote_to_super(member1.id, [])

    def test_promote_to_super_fail_invalid_member_id(self):
        with self.assertRaises(ValueError):
            self.member.promote_to_super(213123, [GroupType.SALES])

    def test_cancel_shift_fail_not_booked(self):
        with self.assertRaises(ValueError):
            self.member.cancel_shift(1, self.member.id)

    def test_add_member_to_group_success(self):
        self.member.add_member_to_group(1, GroupType.CLEANING)
        alice = self.test_db.get("members", [Condition("id", 1)])[0]
        self.assertIn(GroupType.CLEANING, alice.groups)

    def test_remove_member_to_group_success(self):
        self.member.add_member_to_group(1, GroupType.CLEANING)
        self.member.remove_member_from_group(1, GroupType.CLEANING)
        alice = self.test_db.get("members", [Condition("id", 1)])[0]
        self.assertNotIn(GroupType.CLEANING, alice.groups)