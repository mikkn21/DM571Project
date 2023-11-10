from .member import Member
from .shift_create import ShiftCreator
from .enum_group import GroupType
from .shift import Shift

class Super(Member, ShiftCreator):
    def __init__(self, super_groups: GroupType, shiftcreator: ShiftCreator):
        self.super_groups: GroupType = super_groups
        self.__shiftcreator: ShiftCreator = shiftcreator

    def give_free_ticket(member: Member):
        pass

    def create_shift(shift: Shift) -> Shift:
        pass
    
    def promote_to_super(member: Member, group: GroupType):
        pass
    
    def cancel_shift(shift: Shift, member: Member):
        pass
    
    def add_member_to_group(member: Member, group: GroupType) -> Member:
        pass
    
    def remove_member_from_group(member: Member, group: GroupType) -> Member:
        pass
    
    def create_member(member: Member) -> Member:
        pass
    
    def delete_member(member: Member):
        pass
    
    