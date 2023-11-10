from datetime import datetime
from .enum_show_type import ShowType

class Show:
    def __init__(self, title: str, type: ShowType, _from: datetime, _to: datetime, id: int):
        self.title: str = title
        self.type: Show = type
        self._from: datetime = _from
        self._to: datetime = _to
        self.id: int = id
