from datetime import datetime
from .enum_show_type import Show

class Show:
    def __init__(self, title: str, type: Show, _from: datetime, _to: datetime, id: int):
        self.title: str = title
        self.type: Show = type
        self._from: datetime = _from
        self._to: datetime = _to
        self.id: int = id
