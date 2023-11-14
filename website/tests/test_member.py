from django.test import TestCase
from ..models.database import Database, Condition
from ..models.member import Member
from ..models.shift import Shift
from datetime import datetime, timedelta
class MemberTests(TestCase):
    
    def setUp(self):
        # Create a test database instance
        self.test_db = Database()

        # Create some dummy data for testing
        # Dummy members
        self.test_db.insert('members', Member(name='Alice', password='alice123', db=self.test_db))
        self.test_db.insert('members', Member(name='Bob', password='bob123', db=self.test_db))

        # Dummy shifts
        shift1 = Shift(id=1, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=4), 
                       booked_members=[], group=GroupType.SALES, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift1)

        show1 = Show(title="Show1", show_type=ShowType.EVENT, start_date=datetime.now(), 
                 end_date=datetime.now() + timedelta(days=1), id=1)
        self.test_db.insert('shows', show1)

        # Setup a Member instance for tests
        self.member = Member(name='John Doe', password='password123', db=self.test_db)
        self.member.groups.append(GroupType.SALES)


    def test_create_id(self):
        self.assertEqual(self.member.create_id(), 3)  # Assuming IDs start from 1 and two members are already created

    def test_book_shift_success(self):
        self.member.book_shift(1)
        shift = self.test_db.get("shifts", [Condition("id", 1)])[0]
        self.assertIn(self.member.id, shift.booked_members)

    def test_book_shift_fail_capacity(self):
        # Fill the shift to its capacity first
        another_member = self.test_db.get("members", [Condition("name", "Alice")])[0]
        another_member.book_shift(1)

        with self.assertRaises(ExceedingCapacityException):
            self.member.book_shift(1)

    def test_cancel_shift_success(self):
        self.member.book_shift(1)
        self.member.cancel_shift(1)
        shift = self.test_db.get("shifts", [Condition("id", 1)])[0]
        self.assertNotIn(self.member.id, shift.booked_members)

    def test_book_shift_fail_invalid_group(self):
        # Create a shift that requires a different group
        shift2 = Shift(id=2, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=4), 
                    booked_members=[], group=GroupType.TECHNICAL, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift2)

        with self.assertRaises(InvalidGroupException):
            self.member.book_shift(2)

    def test_book_shift_fail_super_shift(self):
        # Create a super shift
        shift3 = Shift(id=3, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=4), 
                    booked_members=[], group=GroupType.SALES, is_super=True, member_capacity=2)
        self.test_db.insert('shifts', shift3)

        with self.assertRaises(MissingAccessRightsException):
            self.member.book_shift(3)

    def test_get_full_schedule(self):
        # Assuming get_full_schedule method is implemented correctly
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=1)
        schedule = self.member.get_full_schedule(start_date, end_date)
        # Assuming Schedule class has 'shows' and 'shifts' attributes
        self.assertTrue(any(show.title == "Show1" for show in schedule.shows))
        self.assertTrue(any(shift.id == 1 for shift in schedule.shifts))

    def test_get_own_schedule(self):
        # Book a shift for the member
        self.member.book_shift(1)
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=1)
        schedule = self.member.get_own_schedule(start_date, end_date)
        self.assertTrue(any(shift.id == 1 for shift in schedule.shifts))
        self.assertTrue(any(show.title == "Show1" for show in schedule.shows))

