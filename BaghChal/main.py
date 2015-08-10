import sys
from Game.Field import *
from Game.Point import Point

if __name__ == "__main__":
    print ("Hello World")

    field = Field()
    print (field)

    field.SetSheep(Point (2,2))
    print (field)