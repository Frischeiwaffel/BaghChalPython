from Game.Figures import *
from Game.Point import *
class Field(object):
    """class describes the gamne field (5x5)"""
    
    def __init__(self, field = None):
        if (field!= None):
            # todo: deep copy
            self.__figures = field.Figures
        else:
            self.__figures=[]
            self.__figures.append(Tiger(Point(0,0)))
            self.__figures.append(Tiger(Point(0,4)))
            self.__figures.append(Tiger(Point(4,0)))
            self.__figures.append(Tiger(Point(4,4)))

    def MoveFigure(self, position, direction):
        pass


    def SetSheep(self,position):
        """Set a sheep on the field"""
        figure = next((i for i in self.__figures if (i.Position.X == position.X and i.Position.Y == position.Y)), None)
        if (figure==None):
            self.__figures.append(Sheep(position))
        else:
            raise InvalidMove("Position already in use")


    def __getFigures(self):
        return self.__figures

    def __str__(self):
        string = ""
        for var_y in range(5):
            
            for var_x in range(5):
                figure = next((i for i in self.__figures if (i.Position.X ==var_x and i.Position.Y == var_y)), None)
                
                string += " "
                
                if(figure is None):
                    string+= " "
                elif (type(figure) is Tiger):
                    string+= "T"
                elif (type(figure) is Sheep):
                    string += "S"

                
                string += " "

                if (var_x!=4):
                    string += "-"
                    pass
                
            string+="\r\n"
            if (var_y == 4):
                return string
            if (var_y%2==0):
                string+= " | \\ | / | \\ | / |\r\n"
            else:
                string+= " | / | \\ | / | \\ |\r\n"
                pass

    Figures = property(__getFigures)

        