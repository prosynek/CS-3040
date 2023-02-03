# Generated from plan.g4 by ANTLR 4.11.1
# encoding: utf-8
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
        4,1,17,147,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,4,0,
        28,8,0,11,0,12,0,29,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,3,1,60,8,1,1,2,1,2,4,2,64,8,2,11,2,12,2,65,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,82,8,3,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,3,5,110,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,
        1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,131,8,8,1,9,
        1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,
        0,0,13,0,2,4,6,8,10,12,14,16,18,20,22,24,0,0,139,0,27,1,0,0,0,2,
        59,1,0,0,0,4,61,1,0,0,0,6,81,1,0,0,0,8,83,1,0,0,0,10,109,1,0,0,0,
        12,111,1,0,0,0,14,114,1,0,0,0,16,130,1,0,0,0,18,132,1,0,0,0,20,138,
        1,0,0,0,22,141,1,0,0,0,24,144,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,
        0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,31,1,0,0,0,31,32,
        3,4,2,0,32,33,5,0,0,1,33,34,6,0,-1,0,34,1,1,0,0,0,35,36,5,8,0,0,
        36,37,3,20,10,0,37,38,5,10,0,0,38,39,5,6,0,0,39,40,3,14,7,0,40,41,
        6,1,-1,0,41,42,6,1,-1,0,42,43,6,1,-1,0,43,44,6,1,-1,0,44,45,6,1,
        -1,0,45,46,6,1,-1,0,46,60,1,0,0,0,47,48,5,8,0,0,48,49,3,20,10,0,
        49,50,5,10,0,0,50,51,5,7,0,0,51,52,3,14,7,0,52,53,6,1,-1,0,53,54,
        6,1,-1,0,54,55,6,1,-1,0,55,56,6,1,-1,0,56,57,6,1,-1,0,57,58,6,1,
        -1,0,58,60,1,0,0,0,59,35,1,0,0,0,59,47,1,0,0,0,60,3,1,0,0,0,61,63,
        5,5,0,0,62,64,3,6,3,0,63,62,1,0,0,0,64,65,1,0,0,0,65,63,1,0,0,0,
        65,66,1,0,0,0,66,5,1,0,0,0,67,68,5,4,0,0,68,69,3,20,10,0,69,70,5,
        12,0,0,70,71,5,9,0,0,71,72,3,8,4,0,72,73,6,3,-1,0,73,82,1,0,0,0,
        74,75,5,4,0,0,75,76,3,20,10,0,76,77,5,12,0,0,77,78,5,8,0,0,78,79,
        3,8,4,0,79,80,6,3,-1,0,80,82,1,0,0,0,81,67,1,0,0,0,81,74,1,0,0,0,
        82,7,1,0,0,0,83,84,5,2,0,0,84,85,3,12,6,0,85,86,6,4,-1,0,86,87,6,
        4,-1,0,87,88,6,4,-1,0,88,89,6,4,-1,0,89,90,6,4,-1,0,90,91,6,4,-1,
        0,91,92,3,10,5,0,92,93,5,15,0,0,93,94,6,4,-1,0,94,9,1,0,0,0,95,96,
        5,1,0,0,96,97,3,12,6,0,97,98,6,5,-1,0,98,99,6,5,-1,0,99,100,6,5,
        -1,0,100,101,6,5,-1,0,101,102,6,5,-1,0,102,103,6,5,-1,0,103,104,
        3,10,5,0,104,105,6,5,-1,0,105,110,1,0,0,0,106,107,3,24,12,0,107,
        108,6,5,-1,0,108,110,1,0,0,0,109,95,1,0,0,0,109,106,1,0,0,0,110,
        11,1,0,0,0,111,112,3,20,10,0,112,113,6,6,-1,0,113,13,1,0,0,0,114,
        115,5,3,0,0,115,116,3,18,9,0,116,117,6,7,-1,0,117,118,3,16,8,0,118,
        119,5,16,0,0,119,120,6,7,-1,0,120,15,1,0,0,0,121,122,5,1,0,0,122,
        123,3,18,9,0,123,124,6,8,-1,0,124,125,3,16,8,0,125,126,6,8,-1,0,
        126,131,1,0,0,0,127,128,3,24,12,0,128,129,6,8,-1,0,129,131,1,0,0,
        0,130,121,1,0,0,0,130,127,1,0,0,0,131,17,1,0,0,0,132,133,3,22,11,
        0,133,134,6,9,-1,0,134,135,5,11,0,0,135,136,3,22,11,0,136,137,6,
        9,-1,0,137,19,1,0,0,0,138,139,5,13,0,0,139,140,6,10,-1,0,140,21,
        1,0,0,0,141,142,5,14,0,0,142,143,6,11,-1,0,143,23,1,0,0,0,144,145,
        1,0,0,0,145,25,1,0,0,0,6,29,59,65,81,109,130
    ]

class planParser ( Parser ):

    grammarFileName = "plan.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'{'", "'['", "'building'", "'complex'", 
                     "'rooms'", "'room'", "'floor'", "'floors'", "'has'", 
                     "'by'", "'with'", "<INVALID>", "<INVALID>", "'}'", 
                     "']'" ]

    symbolicNames = [ "<INVALID>", "COMMA", "LCBRACKET", "LBRACKET", "BUILDING", 
                      "COMPLEX", "ROOMS", "ROOM", "FLOOR", "FLOORS", "HAS", 
                      "BY", "WITH", "NAME", "NUMBER", "RCBRACKET", "RBRACKET", 
                      "WS" ]

    RULE_plan = 0
    RULE_floor = 1
    RULE_complex = 2
    RULE_building = 3
    RULE_floor_list = 4
    RULE_more_floors = 5
    RULE_floor_reference = 6
    RULE_room_list = 7
    RULE_more_rooms = 8
    RULE_room = 9
    RULE_name = 10
    RULE_number = 11
    RULE_empty = 12

    ruleNames =  [ "plan", "floor", "complex", "building", "floor_list", 
                   "more_floors", "floor_reference", "room_list", "more_rooms", 
                   "room", "name", "number", "empty" ]

    EOF = Token.EOF
    COMMA=1
    LCBRACKET=2
    LBRACKET=3
    BUILDING=4
    COMPLEX=5
    ROOMS=6
    ROOM=7
    FLOOR=8
    FLOORS=9
    HAS=10
    BY=11
    WITH=12
    NAME=13
    NUMBER=14
    RCBRACKET=15
    RBRACKET=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PlanContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def complex_(self):
            return self.getTypedRuleContext(planParser.ComplexContext,0)


        def EOF(self):
            return self.getToken(planParser.EOF, 0)

        def floor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(planParser.FloorContext)
            else:
                return self.getTypedRuleContext(planParser.FloorContext,i)


        def getRuleIndex(self):
            return planParser.RULE_plan

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPlan" ):
                listener.enterPlan(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPlan" ):
                listener.exitPlan(self)




    def plan(self):

        localctx = planParser.PlanContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_plan)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.floor()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 31
            self.complex_()
            self.state = 32
            self.match(planParser.EOF)
            output_complex_area()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._name = None # NameContext
            self._room_list = None # Room_listContext

        def FLOOR(self):
            return self.getToken(planParser.FLOOR, 0)

        def name(self):
            return self.getTypedRuleContext(planParser.NameContext,0)


        def HAS(self):
            return self.getToken(planParser.HAS, 0)

        def ROOMS(self):
            return self.getToken(planParser.ROOMS, 0)

        def room_list(self):
            return self.getTypedRuleContext(planParser.Room_listContext,0)


        def ROOM(self):
            return self.getToken(planParser.ROOM, 0)

        def getRuleIndex(self):
            return planParser.RULE_floor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor" ):
                listener.enterFloor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor" ):
                listener.exitFloor(self)




    def floor(self):

        localctx = planParser.FloorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_floor)
        try:
            self.state = 59
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.match(planParser.FLOOR)
                self.state = 36
                localctx._name = self.name()
                self.state = 37
                self.match(planParser.HAS)
                self.state = 38
                self.match(planParser.ROOMS)
                self.state = 39
                localctx._room_list = self.room_list()
                try:
                   check_duplicate_floor(localctx._name.value)
                   floors[localctx._name.value] = localctx._room_list.dimension_list
                except Exception as e:
                   print(e)
                   exit()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(planParser.FLOOR)
                self.state = 48
                localctx._name = self.name()
                self.state = 49
                self.match(planParser.HAS)
                self.state = 50
                self.match(planParser.ROOM)
                self.state = 51
                localctx._room_list = self.room_list()
                try:
                   check_duplicate_floor(localctx._name.value)
                   floors[localctx._name.value] = localctx._room_list.dimension_list
                except Exception as e:
                   print(e)
                   exit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComplexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMPLEX(self):
            return self.getToken(planParser.COMPLEX, 0)

        def building(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(planParser.BuildingContext)
            else:
                return self.getTypedRuleContext(planParser.BuildingContext,i)


        def getRuleIndex(self):
            return planParser.RULE_complex

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComplex" ):
                listener.enterComplex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComplex" ):
                listener.exitComplex(self)




    def complex_(self):

        localctx = planParser.ComplexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_complex)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(planParser.COMPLEX)
            self.state = 63 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.building()
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BuildingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._name = None # NameContext
            self._floor_list = None # Floor_listContext

        def BUILDING(self):
            return self.getToken(planParser.BUILDING, 0)

        def name(self):
            return self.getTypedRuleContext(planParser.NameContext,0)


        def WITH(self):
            return self.getToken(planParser.WITH, 0)

        def FLOORS(self):
            return self.getToken(planParser.FLOORS, 0)

        def floor_list(self):
            return self.getTypedRuleContext(planParser.Floor_listContext,0)


        def FLOOR(self):
            return self.getToken(planParser.FLOOR, 0)

        def getRuleIndex(self):
            return planParser.RULE_building

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuilding" ):
                listener.enterBuilding(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuilding" ):
                listener.exitBuilding(self)




    def building(self):

        localctx = planParser.BuildingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_building)
        try:
            self.state = 81
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.match(planParser.BUILDING)
                self.state = 68
                localctx._name = self.name()
                self.state = 69
                self.match(planParser.WITH)
                self.state = 70
                self.match(planParser.FLOORS)
                self.state = 71
                localctx._floor_list = self.floor_list()
                buildings[localctx._name.value] = localctx._floor_list.floors
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(planParser.BUILDING)
                self.state = 75
                localctx._name = self.name()
                self.state = 76
                self.match(planParser.WITH)
                self.state = 77
                self.match(planParser.FLOOR)
                self.state = 78
                localctx._floor_list = self.floor_list()
                buildings[localctx._name.value] = localctx._floor_list.floors
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Floor_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.floors = None
            self._floor_reference = None # Floor_referenceContext
            self._more_floors = None # More_floorsContext

        def LCBRACKET(self):
            return self.getToken(planParser.LCBRACKET, 0)

        def floor_reference(self):
            return self.getTypedRuleContext(planParser.Floor_referenceContext,0)


        def more_floors(self):
            return self.getTypedRuleContext(planParser.More_floorsContext,0)


        def RCBRACKET(self):
            return self.getToken(planParser.RCBRACKET, 0)

        def getRuleIndex(self):
            return planParser.RULE_floor_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_list" ):
                listener.enterFloor_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_list" ):
                listener.exitFloor_list(self)




    def floor_list(self):

        localctx = planParser.Floor_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_floor_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(planParser.LCBRACKET)
            self.state = 84
            localctx._floor_reference = self.floor_reference()
            try:
               check_valid_floor(localctx._floor_reference.floor_name)
               localctx.floors = [localctx._floor_reference.floor_name]
            except Exception as e:
               print(e)
               exit()
            self.state = 91
            localctx._more_floors = self.more_floors()
            self.state = 92
            self.match(planParser.RCBRACKET)
            localctx.floors = localctx.floors + localctx._more_floors.floors
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_floorsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.floors = None
            self._floor_reference = None # Floor_referenceContext
            self._more_floors = None # More_floorsContext

        def COMMA(self):
            return self.getToken(planParser.COMMA, 0)

        def floor_reference(self):
            return self.getTypedRuleContext(planParser.Floor_referenceContext,0)


        def more_floors(self):
            return self.getTypedRuleContext(planParser.More_floorsContext,0)


        def empty(self):
            return self.getTypedRuleContext(planParser.EmptyContext,0)


        def getRuleIndex(self):
            return planParser.RULE_more_floors

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore_floors" ):
                listener.enterMore_floors(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore_floors" ):
                listener.exitMore_floors(self)




    def more_floors(self):

        localctx = planParser.More_floorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_more_floors)
        try:
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 95
                self.match(planParser.COMMA)
                self.state = 96
                localctx._floor_reference = self.floor_reference()
                try:
                   check_valid_floor(localctx._floor_reference.floor_name)
                   localctx.floors = [localctx._floor_reference.floor_name]
                except Exception as e:
                   print(e)
                   exit()
                self.state = 103
                localctx._more_floors = self.more_floors()
                localctx.floors = localctx.floors + localctx._more_floors.floors
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 106
                self.empty()
                localctx.floors = []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Floor_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.floor_name = None
            self._name = None # NameContext

        def name(self):
            return self.getTypedRuleContext(planParser.NameContext,0)


        def getRuleIndex(self):
            return planParser.RULE_floor_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloor_reference" ):
                listener.enterFloor_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloor_reference" ):
                listener.exitFloor_reference(self)




    def floor_reference(self):

        localctx = planParser.Floor_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_floor_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            localctx._name = self.name()
            localctx.floor_name = localctx._name.value
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Room_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dimension_list = None
            self._room = None # RoomContext
            self._more_rooms = None # More_roomsContext

        def LBRACKET(self):
            return self.getToken(planParser.LBRACKET, 0)

        def room(self):
            return self.getTypedRuleContext(planParser.RoomContext,0)


        def more_rooms(self):
            return self.getTypedRuleContext(planParser.More_roomsContext,0)


        def RBRACKET(self):
            return self.getToken(planParser.RBRACKET, 0)

        def getRuleIndex(self):
            return planParser.RULE_room_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoom_list" ):
                listener.enterRoom_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoom_list" ):
                listener.exitRoom_list(self)




    def room_list(self):

        localctx = planParser.Room_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_room_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(planParser.LBRACKET)
            self.state = 115
            localctx._room = self.room()
            localctx.dimension_list = [localctx._room.dimensions]
            self.state = 117
            localctx._more_rooms = self.more_rooms()
            self.state = 118
            self.match(planParser.RBRACKET)
            localctx.dimension_list = localctx.dimension_list + localctx._more_rooms.dimension_list
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class More_roomsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dimension_list = None
            self._room = None # RoomContext
            self._more_rooms = None # More_roomsContext

        def COMMA(self):
            return self.getToken(planParser.COMMA, 0)

        def room(self):
            return self.getTypedRuleContext(planParser.RoomContext,0)


        def more_rooms(self):
            return self.getTypedRuleContext(planParser.More_roomsContext,0)


        def empty(self):
            return self.getTypedRuleContext(planParser.EmptyContext,0)


        def getRuleIndex(self):
            return planParser.RULE_more_rooms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMore_rooms" ):
                listener.enterMore_rooms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMore_rooms" ):
                listener.exitMore_rooms(self)




    def more_rooms(self):

        localctx = planParser.More_roomsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_more_rooms)
        try:
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 121
                self.match(planParser.COMMA)
                self.state = 122
                localctx._room = self.room()
                localctx.dimension_list = [localctx._room.dimensions]
                self.state = 124
                localctx._more_rooms = self.more_rooms()
                localctx.dimension_list = localctx.dimension_list + localctx._more_rooms.dimension_list
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.empty()
                localctx.dimension_list = []
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RoomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.dimensions = None
            self._number = None # NumberContext

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(planParser.NumberContext)
            else:
                return self.getTypedRuleContext(planParser.NumberContext,i)


        def BY(self):
            return self.getToken(planParser.BY, 0)

        def getRuleIndex(self):
            return planParser.RULE_room

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoom" ):
                listener.enterRoom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoom" ):
                listener.exitRoom(self)




    def room(self):

        localctx = planParser.RoomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_room)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            localctx._number = self.number()
            localctx.dimensions = [localctx._number.value]
            self.state = 134
            self.match(planParser.BY)
            self.state = 135
            localctx._number = self.number()
            localctx.dimensions.append(localctx._number.value)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._NAME = None # Token

        def NAME(self):
            return self.getToken(planParser.NAME, 0)

        def getRuleIndex(self):
            return planParser.RULE_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterName" ):
                listener.enterName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitName" ):
                listener.exitName(self)




    def name(self):

        localctx = planParser.NameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            localctx._NAME = self.match(planParser.NAME)
            localctx.value = (None if localctx._NAME is None else localctx._NAME.text)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._NUMBER = None # Token

        def NUMBER(self):
            return self.getToken(planParser.NUMBER, 0)

        def getRuleIndex(self):
            return planParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = planParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            localctx._NUMBER = self.match(planParser.NUMBER)
            localctx.value = int((None if localctx._NUMBER is None else localctx._NUMBER.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EmptyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return planParser.RULE_empty

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEmpty" ):
                listener.enterEmpty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEmpty" ):
                listener.exitEmpty(self)




    def empty(self):

        localctx = planParser.EmptyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_empty)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





