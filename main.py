import logging 
from dataclasses import dataclass
from collections import OrderedDict

@dataclass
class LivingInfo:
    is_alive: bool=1


class Living:

    hp: int

class Room:
    def interact(self, player: Player):
        player.observe()

class FoodRoom(Room):
    perceivable = OrderedDict(
        {
            'sight': 'You see a pack of edible supplies.',
            'smell': 'You smell food somewhere in the room - you follow the smell until it is under your nose.',
            'touch': 'You sense something small and still behind you - the shape resembles a supply bag that your tribe uses for food storage.',
            'psionic': 'Waves of ravenous hunger and bursting saturation force your movement until you pick up a pearl of gluttony.'
        }
    )
class RestingRoom(Room):
    perceivable = OrderedDict(
        {
            'sight': 'You see an empty room with a huge shelf - you could probably rest in here without being noticed by the forces of evil.',
            'smell': 'You could smell a faint human smell here - someone has probably slept in here. Since it does not smell like blood, you decide it is fine to take a nap here.',
            'sound': 'It is completely silent in this room. You could probably rest in here, at least until you hear something.',
            'psionic': 'A caleidoscope is all around you. You are in it. And you are around it. Lie down and enjoy it.'
        }
    )

class AltarRoom(Room):
    perceivable = OrderedDict(
        {
            'sight': 'You see a painfully exquisite alien altar in the middle of the room.',
            'psionic': 'Awareness of an angelic presence comes through your mind like an excruciating shockwave of pleasure.',
            'sound': 'You hear an entrancing incomprehensible noise that entices you to follow it',
            'smell': 'The horrifying fragrant scent is forcing you to follow it',
            'touch': 'You can\t stop enjoying the unbearable pain you feel under your hands'
        }
    )

class Human(Living):

    hp: int=10
    wp: int=10
    pass 

@dataclass
class RoomInfo:

    # actual room from the objective reality
    room: Room
    # our perception of it
    food: bool=0
    rest: bool=0
    living_obstacle: bool=0
    altar: bool=0



class Player(Human):
    def _room_loop(self, room: Room):
        room_info = self.observe(room)
        room_info = self.select_action(room_info)
        room_info = self.select_path(room_info)
    
    def observe(self, room: Room) -> RoomInfo:
        pass
    
    def select_action(self, room_info: RoomInfo):
        pass

        
        


