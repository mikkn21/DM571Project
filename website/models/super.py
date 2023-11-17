from ast import Set
from .member import Member
from .shift_create import ShiftCreator
from .enum_group import GroupType
from .shift import Shift
from database import Condition

class Super(Member):
    def __init__(self, super_groups: GroupType, shiftcreator: ShiftCreator):
        super.__init__()
        self.is_super = True
        self.super_groups: Set[GroupType] = super_groups
        self.__shift_creator: 'ShiftCreator' = shiftcreator

    def give_free_ticket(self, member_id: int) -> None:
        member = self.__get_element_by_id("members", member_id)
        self.db.update("members", [Condition("id", member_id)], {"free_ticket": member.free_ticket+1})

    def create_shift(shift: Shift) -> Shift:
        pass 

    def add_super_to_group(self, member_id: int, group: GroupType) -> None:
        member = self.db.get("members", [Condition("id", member_id)])[0]
        if not member.is_super:
            raise AttributeError("Member was not a Super")
        self.db.update("member", [Condition("id", member_id)], {"self"})

    
    def promote_to_super(self, member_id: int, group: GroupType) -> None:
        member = self.__get_element_by_id("members", member_id)
        try:
            member.super_groups.append(group)
        except AttributeError as e:
            raise AttributeError("Member was not a Super")
        
        
    def cancel_shift(shift: Shift, member: Member) -> None:
        pass
    
    def add_member_to_group(member: Member, group: GroupType) -> Member:
        pass
    
    def remove_member_from_group(member: Member, group: GroupType) -> Member:
        pass
    
    def create_member(member: Member) -> Member:
        pass
    
    def delete_member(member: Member) -> None:
        pass
    
    