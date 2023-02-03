# Generated from plan.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .planParser import planParser
else:
    from planParser import planParser

"""
- CS3040 - 001
- Fall 2022
- Assignment 4 - Complex ANTLRs
- Name: Paige Rosynek
- Date: 11.10.2022
"""
buildings = {}
floors = {}

def check_valid_floor(floor):
        """
        Checks if floor specified in builing exists in the list of floors
        
        :param str floor: floor name to check
        :raises Exception: if floor does not exist in the list of floors
        """
        if floor not in list(floors.keys()):
            raise Exception(f'Reference to missing floor {floor}')


def check_duplicate_floor(floor):
    """
        Checks if floor is already specified in the list of floors
        
        :param str floor: floor name to check
        :raises Exception: if floor exists in the list of floors
    """
    if floor in floors.keys():
        raise Exception(f'Duplicate floor {floor}')
        

def output_complex_area():
    """
    Calculates and outputs the area of each building and the total area of the complex for a valid input string
    """
    total_area = 0
    for building, floor_list in buildings.items():
        area = 0
        for floor in floor_list:
            rooms = floors[floor] 
            area += sum(map(lambda room: int(room[0]) * int(room[1]), rooms))
            
        total_area += area
        print(f'Area for building {building}: {area} square feet.')
    
    print(f'Total area: {total_area} square feet.')


# This class defines a complete listener for a parse tree produced by planParser.
class planListener(ParseTreeListener):

    # Enter a parse tree produced by planParser#plan.
    def enterPlan(self, ctx:planParser.PlanContext):
        pass

    # Exit a parse tree produced by planParser#plan.
    def exitPlan(self, ctx:planParser.PlanContext):
        pass


    # Enter a parse tree produced by planParser#floor.
    def enterFloor(self, ctx:planParser.FloorContext):
        pass

    # Exit a parse tree produced by planParser#floor.
    def exitFloor(self, ctx:planParser.FloorContext):
        pass


    # Enter a parse tree produced by planParser#complex.
    def enterComplex(self, ctx:planParser.ComplexContext):
        pass

    # Exit a parse tree produced by planParser#complex.
    def exitComplex(self, ctx:planParser.ComplexContext):
        pass


    # Enter a parse tree produced by planParser#building.
    def enterBuilding(self, ctx:planParser.BuildingContext):
        pass

    # Exit a parse tree produced by planParser#building.
    def exitBuilding(self, ctx:planParser.BuildingContext):
        pass


    # Enter a parse tree produced by planParser#floor_list.
    def enterFloor_list(self, ctx:planParser.Floor_listContext):
        pass

    # Exit a parse tree produced by planParser#floor_list.
    def exitFloor_list(self, ctx:planParser.Floor_listContext):
        pass


    # Enter a parse tree produced by planParser#more_floors.
    def enterMore_floors(self, ctx:planParser.More_floorsContext):
        pass

    # Exit a parse tree produced by planParser#more_floors.
    def exitMore_floors(self, ctx:planParser.More_floorsContext):
        pass


    # Enter a parse tree produced by planParser#floor_reference.
    def enterFloor_reference(self, ctx:planParser.Floor_referenceContext):
        pass

    # Exit a parse tree produced by planParser#floor_reference.
    def exitFloor_reference(self, ctx:planParser.Floor_referenceContext):
        pass


    # Enter a parse tree produced by planParser#room_list.
    def enterRoom_list(self, ctx:planParser.Room_listContext):
        pass

    # Exit a parse tree produced by planParser#room_list.
    def exitRoom_list(self, ctx:planParser.Room_listContext):
        pass


    # Enter a parse tree produced by planParser#more_rooms.
    def enterMore_rooms(self, ctx:planParser.More_roomsContext):
        pass

    # Exit a parse tree produced by planParser#more_rooms.
    def exitMore_rooms(self, ctx:planParser.More_roomsContext):
        pass


    # Enter a parse tree produced by planParser#room.
    def enterRoom(self, ctx:planParser.RoomContext):
        pass

    # Exit a parse tree produced by planParser#room.
    def exitRoom(self, ctx:planParser.RoomContext):
        pass


    # Enter a parse tree produced by planParser#name.
    def enterName(self, ctx:planParser.NameContext):
        pass

    # Exit a parse tree produced by planParser#name.
    def exitName(self, ctx:planParser.NameContext):
        pass


    # Enter a parse tree produced by planParser#number.
    def enterNumber(self, ctx:planParser.NumberContext):
        pass

    # Exit a parse tree produced by planParser#number.
    def exitNumber(self, ctx:planParser.NumberContext):
        pass


    # Enter a parse tree produced by planParser#empty.
    def enterEmpty(self, ctx:planParser.EmptyContext):
        pass

    # Exit a parse tree produced by planParser#empty.
    def exitEmpty(self, ctx:planParser.EmptyContext):
        pass



del planParser