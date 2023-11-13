from datetime import datetime
from .enum_show_type import ShowType

class Show:
    def __init__(self, title: str, show_type: ShowType, start_date: datetime, end_date: datetime, id: int):
        self.title: str = title
        self.show_type: ShowType = show_type
        self.start_date: datetime = start_date
        self.end_date: datetime = end_date
        self.id: int = id
