from website.models.database import Database, Condition
from website.models.show import Show
from website.models.enum_show_type import ShowType
from datetime import datetime


def database_test():
    db = Database()
    db.insert("shows", Show("e", ShowType.EVENT, datetime.now(), datetime.now(),  2))
    db.insert("shows", Show("q", ShowType.PREMIERE, datetime.now(), datetime.now(),  587))
    db.insert("shows", Show("w", ShowType.EVENT, datetime.now(), datetime.now(),  6))
    db.insert("shows", Show("w", ShowType.EVENT, datetime.now(), datetime.now(),  7))
    db.insert("shows", Show("t", ShowType.EVENT, datetime.now(), datetime.now(),  8))


    print([k.id for k in db._data["shows"]])
    db.delete("shows", [Condition("id", 2)])

    print([k.id for k in db._data["shows"]])

    print([s.id for s in db.get("shows", [Condition("title", "w"), Condition("show_type", ShowType.EVENT)])])

#    print([k.id for k in db._data["shows"]])

database_test()