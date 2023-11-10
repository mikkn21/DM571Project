from member import Member
from shift_create import ShiftCreator
from enum_group import Group
from shift import Shift

class Super(Member, ShiftCreator):
    def __init__(self, super_groups: Group, shiftcreator: ShiftCreator):
        self.super_groups: Group = super_groups
        self.__shiftcreator: ShiftCreator = shiftcreator

    def give_free_ticket(member: Member):
        pass

    def create_shift(shift: Shift) -> Shift:
        pass
    
    def promote_to_super(member: Member, group: Group):
        pass
    
    def cancel_shift(shift: Shift, member: Member):
        pass
    
    def add_member_to_group(member: Member, group: Group) -> Member:
        pass
    
    def remove_member_from_group(member: Member, group: Group) -> Member:
        pass
    
    def create_member(member: Member) -> Member:
        pass
    
    def delete_member(member: Member):
        pass
    
    