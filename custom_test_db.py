from website.models.database import Database, Condition
from website.models.enum_group import GroupType
from website.models.shift import Shift
from website.models.show import Show
from website.models.enum_show_type import ShowType
from datetime import datetime, timedelta


def database_test():
    db = Database()
    db.insert("shows", Show("e", ShowType.EVENT, datetime.now(), datetime.now(), db))
    db.insert("shows", Show("q", ShowType.PREMIERE, datetime.now(), datetime.now(), db))
    db.insert("shows", Show("w", ShowType.EVENT, datetime.now(), datetime.now(), db))
    db.insert("shows", Show("w", ShowType.EVENT, datetime.now(), datetime.now(), db))
    db.insert("shows", Show("t", ShowType.EVENT, datetime.now(), datetime.now(), db))
    db.insert("shifts", Shift(db, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.CLEANING, False, 5))
    db.insert("shifts", Shift(db, datetime.now(), datetime.now() + timedelta(days=7), [1,2,3,4,5], GroupType.PR, False, 5))

    print([s.id for s in db.get("shows", [])])
    print([s.id for s in db.get("shifts", [])])


#    print([k.id for k in db._data["shows"]])

database_test()