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

        # Create some dummy data for testing
        # Dummy members
        alice = Member(name='Alice', password='alice123', db=self.test_db, email="alice@gmail.cm", phone_number="+69420420")
        alice.groups.add(GroupType.SALES)
        self.test_db.insert('members', alice)
        self.test_db.insert('members', Member(name='Bob', password='bob123', db=self.test_db, email="bob123@gmail.com", phone_number="+4598126578"))

        # Setup a Member instance for tests
        self.member = Member(name='John Doe', password='password123', db=self.test_db, email="JoDo@hotmail.com", phone_number="+4512345678")
        self.member.groups.add(GroupType.SALES)

        # Dummy shifts
        shift1 = Shift(self.test_db, start_date=datetime.now() + timedelta(days=8), end_date=datetime.now() + timedelta(days=8,hours=4), 
                       booked_members=[], group=GroupType.SALES, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift1)

        show1 = Show(db=self.test_db, title="Show1", show_type=ShowType.EVENT, start_date=datetime.now(), 
                 end_date=datetime.now() + timedelta(days=1))
        self.test_db.insert('shows', show1)

    # Remember to change how shifts and shows are created once ID creation has been implemented!!!

    def test_book_shift_success(self):
        self.member.book_shift(1)
        shift = self.test_db.get("shifts", [Condition("id", 1)])[0]
        self.assertIn(self.member.id, shift.booked_members)

    def test_book_shift_fail_capacity(self):
        # Fill the shift to its capacity first
        another_member: Member = self.test_db.get("members", [Condition("name", "Alice")])[0]
        another_member.book_shift(1)
        another_member2: Member = self.test_db.get("members", [Condition("name", "Bob")])[0]
        another_member2.groups.add(GroupType.SALES)
        another_member2.book_shift(1)
        with self.assertRaises(ExceedingCapacityException):
            self.member.book_shift(1)
    
    def test_book_shift_fail_outdated(self):
        # Create a shift that is too old
        another_shift = Shift(self.test_db, start_date=datetime.now() - timedelta(days=2), end_date=datetime.now() - timedelta(days=1), 
                       booked_members=[], group=GroupType.SALES, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', another_shift)

        with self.assertRaises(OutdatedActionException):
            self.member.book_shift(2)

    def test_book_shift_fail_invalid_group(self):
        # Create a shift that requires a different group
        shift2 = Shift(self.test_db, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=4), 
                    booked_members=[], group=GroupType.TECHNICAL, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift2)

        with self.assertRaises(InvalidGroupException):
            self.member.book_shift(2)

    def test_book_shift_fail_super_shift(self):
        # Create a super shift
        shift2 = Shift(self.test_db, start_date=datetime.now(), end_date=datetime.now() + timedelta(hours=4), 
                    booked_members=[], group=GroupType.SALES, is_super=True, member_capacity=2)
        self.test_db.insert('shifts', shift2)

        with self.assertRaises(MissingAccessRightsException):
            self.member.book_shift(2)

    def test_book_shift_fail_double_book(self):
        self.member.book_shift(1)
        with self.assertRaises(ExceedingCapacityException):
            self.member.book_shift(1)

    def test_get_full_schedule_success(self):
        # Assuming get_full_schedule method is implemented correctly
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=10)
        schedule = self.member.get_full_schedule(start_date, end_date)
        # Assuming Schedule class has 'shows' and 'shifts' attributes
        self.assertTrue(any(show.title == "Show1" for show in schedule.shows))
        self.assertTrue(any(shift.id == 1 for shift in schedule.shifts))

    def test_get_full_schedule_fail_invalid_datetime(self):
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() - timedelta(days=2)

        with self.assertRaises(ValueError):
            self.member.get_full_schedule(start_date, end_date)

    # Maybe make a test for returning an empty schedule???

    def test_get_own_schedule_success(self):
        # Book a shift for the member
        self.member.book_shift(1)
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() + timedelta(days=10)
        schedule = self.member.get_own_schedule(start_date, end_date)
        self.assertTrue(any(shift.id == 1 for shift in schedule.shifts))
        self.assertTrue(any(show.title == "Show1" for show in schedule.shows))

    def test_get_own_schedule_fail_outdated(self):
        # Book a shift for the member
        self.member.book_shift(1)
        start_date = datetime.now() - timedelta(days=1)
        end_date = datetime.now() - timedelta(days=2)

        with self.assertRaises(ValueError):
            self.member.get_own_schedule(start_date, end_date)

    def test_cancel_shift_fail_outdated(self):
        # Create a shift that is too old
        shift2 = Shift(self.test_db, start_date=datetime.now() - timedelta(days=2), end_date=datetime.now() - timedelta(days=1), 
                       booked_members=[], group=GroupType.SALES, is_super=False, member_capacity=2)
        self.test_db.insert('shifts', shift2)

        with self.assertRaises(OutdatedActionException):
            self.member.cancel_shift(2)

    def test_cancel_shift_fail_not_booked(self):
        with self.assertRaises(ValueError):
            self.member.cancel_shift(1)

    def test_cancel_shift_success(self):
        self.member.book_shift(1)
        self.member.cancel_shift(1)
        shift = self.test_db.get("shifts", [Condition("id", 1)])[0]
        self.assertNotIn(self.member.id, shift.booked_members)


    def test_get_free_tickets_remaining_count_success(self):
        self.assertEqual(self.member.get_free_tickets_remaining_count(), 0)

    def test_valid_phone_number_failure(self):
        with self.assertRaises(ValueError):
            test_member: Member = Member(name="Testman", password="lmao", db=self.test_db, email="lmao123@gmail.com", phone_number="+abc")

    def test_unique_email_success(self):
        self.test_db.insert("members",self.member)
        john: Member = self.test_db.get("members", [Condition("id", self.member.id)])[0]
        self.assertEqual(john.email, self.member.email)
        self.assertEqual(self.test_db.get("members", [Condition("email", "alice@gmail.cm")])[0].email, "alice@gmail.cm")
        
    def test_unique_email_failed(self):
        self.test_db.insert("members",self.member)
        with self.assertRaises(ValueError):
            Member(name='John Doe', password='password123', db=self.test_db, email="JoDo@hotmail.com", phone_number="+4512345678")

