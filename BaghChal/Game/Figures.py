from Game.Point import Point
from Game.Exceptions import *


class Figure(object):
    """abstract class describes figure defined by its position"""
    
    def __init__(self, position):
        self.Position= position


    #private methodes

    def _set_position(self, position):
        #check if position is on field
        if (0 <= position.X < 5 and 0 <= position.Y < 5):
            self.__position = position
        else:
            raise InvalidMove("Position is out of field!")
    def _get_position(self):
        return self.__position
    

    # properties
    Position = property(_get_position,_set_position)     


class Sheep(Figure):
    """ class describes the sheep figure of the game """

    def __init__(self, position):
        return super().__init__(position)

    def _set_position(self,position):
        #check if new position is in reach of the old position
        Figure._set_position(self,position)
    

    Position = property(Figure._get_position,_set_position)

class Tiger(Figure):
    """ class describes the Tiger figure of the game """
    def __init__(self, position):
        self.Position = position
    
    def _set_position(self,position):
        #check if new position is in reach of the old position
        Figure._set_position(self,position)

    Position = property(Figure._get_position,_set_position)



