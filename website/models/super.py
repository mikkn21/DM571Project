from typing import Set

from ..models.custom_exception import InvalidGroupException
from .member import Member
from .shift_creator import ShiftCreator
from .enum_group import GroupType
from .shift import Shift
from .database import Condition, Database
from typing import List
from website.models import shift_creator

class Super(Member):
    def __init__(self, name: str, password: str, db: Database, email: str, phone_number: str, super_groups: Set[GroupType], shift_creator: ShiftCreator):
        super().__init__(name, password, db, email, phone_number)
        self.is_super = True
        self.super_groups: Set[GroupType] = super_groups
        self.__shift_creator: ShiftCreator = shift_creator

    def give_free_ticket(self, member_id: int) -> None:
        member = self._get_element_by_id("members", member_id)
        self.db.update("members", [Condition("id", member_id)], {"obtained_free_tickets": member.obtained_free_tickets+1})

    def create_shift(self, shift: Shift):
        self.__shift_creator.create_shift(shift)

    def add_super_to_group(self, member_id: int, group: GroupType) -> None:
        _super = self.db.get("members", [Condition("id", member_id)])[0]
        if group in _super.super_groups:
            raise ValueError("Super was already part of that group")
        _super.super_groups.add(group)
        self.db.update("members", [Condition("id", member_id)], {"super_groups": _super.super_groups})
    
    def promote_to_super(self, member_id: int, super_groups: List[GroupType]) -> None:
        if not super_groups:
            raise InvalidGroupException("No groups to be super for was given. List must not be empty")
        member = self._get_element_by_id("members", member_id)
        self.db.delete("members", [Condition("id", member.id)])
        _super = Super(member.name, "123", member.db, member.email, member.phone_number, super_groups, self.__shift_creator)
        _super.password = member.password
        self.db.insert("members", _super)
        
    def cancel_shift(self, shift_id: int, member_id: int) -> None:
        shift: "Shift" = self._get_element_by_id("shifts", shift_id)
        if member_id not in shift.booked_members:
            raise ValueError("Member cannot cancel a shift, that they have not booked")
        else:
            shift.booked_members.remove(member_id)
            self.db.update("shifts", [Condition("id", shift.id)], {"booked_members": shift.booked_members})
    
    def add_member_to_group(self, member_id: int, group: GroupType) -> None:
        member1 = self._get_element_by_id("members", member_id)
        if group not in member1.groups:
            member1.groups.add(group)
            self.db.update("members", [Condition("id", member_id)], {"groups": member1.groups})
    
    def remove_member_from_group(self, member_id: int, group: GroupType) -> None:
        member1 = self._get_element_by_id("members", member_id)
        if group in member1.groups:
            member1.groups.remove(group)
            self.db.update("members", [Condition("id", member_id)], {"groups": member1.groups})
    
    def create_member(self, member: Member) -> None:
        self.db.insert("members", member)
    
    def delete_member(self, member_id: int) -> None:
        self.db.delete("members", [Condition("id", member_id)])
    
    