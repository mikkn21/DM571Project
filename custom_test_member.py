from website.models.database import Database, Condition
from website.models.password_protection import check_password
from website.models.show import Show
from website.models.shift import Shift
from website.models.enum_show_type import ShowType
from website.models.enum_group import GroupType
from website.models.member import Member
from datetime import datetime
from datetime import timedelta

def database_test():
    db = Database()
    db.insert("shows", Show("e", ShowType.EVENT, datetime.now(), datetime.now(),  2))
    db.insert("shows", Show("q", ShowType.PREMIERE, datetime.now(), datetime.now(),  587))
    db.insert("shows", Show("w", ShowType.EVENT, datetime.now(), datetime.now(),  6))
    db.insert("shows", Show("w", ShowType.EVENT, datetime.now(), datetime.now(),  7))
    db.insert("shows", Show("t", ShowType.EVENT, datetime.now(), datetime.now(),  8))

    db.insert("shifts", Shift(1, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.CLEANING, False, 5))
    db.insert("shifts", Shift(3, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(4, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(5, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(6, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(7, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(8, datetime.now() - timedelta(days=1), datetime.now() + timedelta(days=1), [1,2,3,4,5], GroupType.SALES, False, 5))
    db.insert("shifts", Shift(9, datetime.now() - timedelta(days=7), datetime.now(), [5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(10, datetime.now() - timedelta(days=7), datetime.now(), [5], GroupType.PR, False, 5))
    db.insert("shifts", Shift(11, datetime.now() - timedelta(days=7), datetime.now(), [5], GroupType.PR, False, 5))
    member: Member = Member("Malthe", "lmao", db)
    db.insert("members", member)
    member.groups.append(GroupType.SALES)
    member = db.get("Members", [Condition("id", id)])[0]
    check_password("lmao", member.password)

    
database_test()