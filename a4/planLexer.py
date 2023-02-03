# Generated from plan.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


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


def serializedATN():
    return [
        4,0,17,115,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,1,0,1,0,1,1,1,1,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,10,1,10,1,10,
        1,11,1,11,1,11,1,11,1,11,1,12,4,12,96,8,12,11,12,12,12,97,1,13,4,
        13,101,8,13,11,13,12,13,102,1,14,1,14,1,15,1,15,1,16,4,16,110,8,
        16,11,16,12,16,111,1,16,1,16,0,0,17,1,1,3,2,5,3,7,4,9,5,11,6,13,
        7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,1,0,
        2,2,0,65,90,95,95,3,0,9,10,13,13,32,32,117,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,
        1,35,1,0,0,0,3,37,1,0,0,0,5,39,1,0,0,0,7,41,1,0,0,0,9,50,1,0,0,0,
        11,58,1,0,0,0,13,64,1,0,0,0,15,69,1,0,0,0,17,75,1,0,0,0,19,82,1,
        0,0,0,21,86,1,0,0,0,23,89,1,0,0,0,25,95,1,0,0,0,27,100,1,0,0,0,29,
        104,1,0,0,0,31,106,1,0,0,0,33,109,1,0,0,0,35,36,5,44,0,0,36,2,1,
        0,0,0,37,38,5,123,0,0,38,4,1,0,0,0,39,40,5,91,0,0,40,6,1,0,0,0,41,
        42,5,98,0,0,42,43,5,117,0,0,43,44,5,105,0,0,44,45,5,108,0,0,45,46,
        5,100,0,0,46,47,5,105,0,0,47,48,5,110,0,0,48,49,5,103,0,0,49,8,1,
        0,0,0,50,51,5,99,0,0,51,52,5,111,0,0,52,53,5,109,0,0,53,54,5,112,
        0,0,54,55,5,108,0,0,55,56,5,101,0,0,56,57,5,120,0,0,57,10,1,0,0,
        0,58,59,5,114,0,0,59,60,5,111,0,0,60,61,5,111,0,0,61,62,5,109,0,
        0,62,63,5,115,0,0,63,12,1,0,0,0,64,65,5,114,0,0,65,66,5,111,0,0,
        66,67,5,111,0,0,67,68,5,109,0,0,68,14,1,0,0,0,69,70,5,102,0,0,70,
        71,5,108,0,0,71,72,5,111,0,0,72,73,5,111,0,0,73,74,5,114,0,0,74,
        16,1,0,0,0,75,76,5,102,0,0,76,77,5,108,0,0,77,78,5,111,0,0,78,79,
        5,111,0,0,79,80,5,114,0,0,80,81,5,115,0,0,81,18,1,0,0,0,82,83,5,
        104,0,0,83,84,5,97,0,0,84,85,5,115,0,0,85,20,1,0,0,0,86,87,5,98,
        0,0,87,88,5,121,0,0,88,22,1,0,0,0,89,90,5,119,0,0,90,91,5,105,0,
        0,91,92,5,116,0,0,92,93,5,104,0,0,93,24,1,0,0,0,94,96,7,0,0,0,95,
        94,1,0,0,0,96,97,1,0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,26,1,0,0,
        0,99,101,2,48,57,0,100,99,1,0,0,0,101,102,1,0,0,0,102,100,1,0,0,
        0,102,103,1,0,0,0,103,28,1,0,0,0,104,105,5,125,0,0,105,30,1,0,0,
        0,106,107,5,93,0,0,107,32,1,0,0,0,108,110,7,1,0,0,109,108,1,0,0,
        0,110,111,1,0,0,0,111,109,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,
        0,113,114,6,16,0,0,114,34,1,0,0,0,4,0,97,102,111,1,0,1,0
    ]

class planLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    COMMA = 1
    LCBRACKET = 2
    LBRACKET = 3
    BUILDING = 4
    COMPLEX = 5
    ROOMS = 6
    ROOM = 7
    FLOOR = 8
    FLOORS = 9
    HAS = 10
    BY = 11
    WITH = 12
    NAME = 13
    NUMBER = 14
    RCBRACKET = 15
    RBRACKET = 16
    WS = 17

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'{'", "'['", "'building'", "'complex'", "'rooms'", "'room'", 
            "'floor'", "'floors'", "'has'", "'by'", "'with'", "'}'", "']'" ]

    symbolicNames = [ "<INVALID>",
            "COMMA", "LCBRACKET", "LBRACKET", "BUILDING", "COMPLEX", "ROOMS", 
            "ROOM", "FLOOR", "FLOORS", "HAS", "BY", "WITH", "NAME", "NUMBER", 
            "RCBRACKET", "RBRACKET", "WS" ]

    ruleNames = [ "COMMA", "LCBRACKET", "LBRACKET", "BUILDING", "COMPLEX", 
                  "ROOMS", "ROOM", "FLOOR", "FLOORS", "HAS", "BY", "WITH", 
                  "NAME", "NUMBER", "RCBRACKET", "RBRACKET", "WS" ]

    grammarFileName = "plan.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


