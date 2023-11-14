from django.test import TestCase
from ..models.database import Database, Condition
from ..models.member import Member
from ..models.shift import Shift

class DatabaseTestCase(TestCase):
    def setUp(self):
        self.db = Database()
        self.db.insert('members', Member("Malthe", "lmao", self.db))
        self.db.insert('members', Member("Sofus", "123", self.db))

    def test_insert(self):
        self.assertEqual(len(self.db._data['members']), 2)

    def test_delete(self):
        condition = Condition(key='name', value='Sofus')
        self.db.delete('members', [condition])
        self.assertEqual(len(self.db._data['members']), 1)

    # Add more tests for update, get, and other functionalities

class ConditionTestCase(TestCase):
    def test_initialization(self):
        condition = Condition(key='name', value='Alice')
        self.assertEqual(condition.key, 'name')
        self.assertEqual(condition.value, 'Alice')

    def test_custom_comparison_function(self):
        condition = Condition(key='name', value='Alice', compare=lambda x, y: x != y)
        self.assertFalse(condition.compare('Alice', 'Alice'))

    # Add more tests as needed
