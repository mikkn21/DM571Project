from datetime import datetime
from ..models.database import Condition, Database
from .enum_show_type import ShowType

class Show:
    def __init__(self, title: str, show_type: ShowType, start_date: datetime, end_date: datetime, db: Database):
        self.title: str = title
        self.show_type: ShowType = show_type
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date
        self.db = db
        self.id: int = self.__create_id()


    def __create_id(self):
        ids = self.db.get("ids", [Condition("key", "shows")])
        if len(ids) != 1:
            raise ValueError("invalid amount of ids for show in database")
        new_id = ids[0].value+1
        self.db.update("ids", [Condition("key", "shows")], {"value": new_id})
        return new_id
