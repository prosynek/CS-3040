# Generated from adder2.g4 by ANTLR 4.11.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,0,4,0,25,8,0,11,0,
        12,0,26,1,0,1,0,3,0,31,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,4,1,4,1,4,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,66,8,6,1,7,1,7,1,7,1,7,0,0,8,
        0,2,4,6,8,10,12,14,0,0,67,0,30,1,0,0,0,2,32,1,0,0,0,4,36,1,0,0,0,
        6,49,1,0,0,0,8,51,1,0,0,0,10,54,1,0,0,0,12,65,1,0,0,0,14,67,1,0,
        0,0,16,18,3,2,1,0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,
        1,0,0,0,20,21,1,0,0,0,21,22,5,0,0,1,22,31,1,0,0,0,23,25,3,4,2,0,
        24,23,1,0,0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,28,1,
        0,0,0,28,29,5,0,0,1,29,31,1,0,0,0,30,17,1,0,0,0,30,24,1,0,0,0,31,
        1,1,0,0,0,32,33,5,1,0,0,33,34,3,12,6,0,34,35,6,1,-1,0,35,3,1,0,0,
        0,36,37,5,2,0,0,37,38,3,6,3,0,38,39,6,2,-1,0,39,40,6,2,-1,0,40,5,
        1,0,0,0,41,42,3,10,5,0,42,43,6,3,-1,0,43,50,1,0,0,0,44,45,3,10,5,
        0,45,46,5,3,0,0,46,47,3,8,4,0,47,48,6,3,-1,0,48,50,1,0,0,0,49,41,
        1,0,0,0,49,44,1,0,0,0,50,7,1,0,0,0,51,52,3,6,3,0,52,53,6,4,-1,0,
        53,9,1,0,0,0,54,55,5,5,0,0,55,56,6,5,-1,0,56,11,1,0,0,0,57,58,3,
        14,7,0,58,59,6,6,-1,0,59,66,1,0,0,0,60,61,3,14,7,0,61,62,5,3,0,0,
        62,63,3,12,6,0,63,64,6,6,-1,0,64,66,1,0,0,0,65,57,1,0,0,0,65,60,
        1,0,0,0,66,13,1,0,0,0,67,68,5,4,0,0,68,69,6,7,-1,0,69,15,1,0,0,0,
        5,19,26,30,49,65
    ]

class adder2Parser ( Parser ):

    grammarFileName = "adder2.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "','" ]

    symbolicNames = [ "<INVALID>", "ADD", "AVE", "COMMA", "INTEGER", "FLOAT", 
                      "WS" ]

    RULE_commands = 0
    RULE_addCommand = 1
    RULE_aveCommand = 2
    RULE_float_list = 3
    RULE_rest_of_float_list = 4
    RULE_float_num = 5
    RULE_integer_list = 6
    RULE_integer = 7

    ruleNames =  [ "commands", "addCommand", "aveCommand", "float_list", 
                   "rest_of_float_list", "float_num", "integer_list", "integer" ]

    EOF = Token.EOF
    ADD=1
    AVE=2
    COMMA=3
    INTEGER=4
    FLOAT=5
    WS=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class CommandsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(adder2Parser.EOF, 0)

        def addCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(adder2Parser.AddCommandContext)
            else:
                return self.getTypedRuleContext(adder2Parser.AddCommandContext,i)


        def aveCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(adder2Parser.AveCommandContext)
            else:
                return self.getTypedRuleContext(adder2Parser.AveCommandContext,i)


        def getRuleIndex(self):
            return adder2Parser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)




    def commands(self):

        localctx = adder2Parser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 16
                    self.addCommand()
                    self.state = 19 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 21
                self.match(adder2Parser.EOF)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 23
                    self.aveCommand()
                    self.state = 26 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break

                self.state = 28
                self.match(adder2Parser.EOF)
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


    class AddCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._integer_list = None # Integer_listContext

        def ADD(self):
            return self.getToken(adder2Parser.ADD, 0)

        def integer_list(self):
            return self.getTypedRuleContext(adder2Parser.Integer_listContext,0)


        def getRuleIndex(self):
            return adder2Parser.RULE_addCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddCommand" ):
                listener.enterAddCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddCommand" ):
                listener.exitAddCommand(self)




    def addCommand(self):

        localctx = adder2Parser.AddCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_addCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(adder2Parser.ADD)
            self.state = 33
            localctx._integer_list = self.integer_list()
            print("Sum: " + str(localctx._integer_list.list_value))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AveCommandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._float_list = None # Float_listContext

        def AVE(self):
            return self.getToken(adder2Parser.AVE, 0)

        def float_list(self):
            return self.getTypedRuleContext(adder2Parser.Float_listContext,0)


        def getRuleIndex(self):
            return adder2Parser.RULE_aveCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAveCommand" ):
                listener.enterAveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAveCommand" ):
                listener.exitAveCommand(self)




    def aveCommand(self):

        localctx = adder2Parser.AveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_aveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(adder2Parser.AVE)
            self.state = 37
            localctx._float_list = self.float_list()
            print(localctx._float_list.list_)
            print("Average: " + str(sum(localctx._float_list.list_) / len(localctx._float_list.list_)))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_ = None
            self._float_num = None # Float_numContext

        def float_num(self):
            return self.getTypedRuleContext(adder2Parser.Float_numContext,0)


        def COMMA(self):
            return self.getToken(adder2Parser.COMMA, 0)

        def rest_of_float_list(self):
            return self.getTypedRuleContext(adder2Parser.Rest_of_float_listContext,0)


        def getRuleIndex(self):
            return adder2Parser.RULE_float_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_list" ):
                listener.enterFloat_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_list" ):
                listener.exitFloat_list(self)




    def float_list(self):

        localctx = adder2Parser.Float_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_float_list)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                localctx._float_num = self.float_num()
                localctx.list_ = [localctx._float_num.value]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                localctx._float_num = self.float_num()
                self.state = 45
                self.match(adder2Parser.COMMA)
                self.state = 46
                self.rest_of_float_list()
                localctx.list_.append(localctx._float_num.value)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rest_of_float_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_ = None

        def float_list(self):
            return self.getTypedRuleContext(adder2Parser.Float_listContext,0)


        def getRuleIndex(self):
            return adder2Parser.RULE_rest_of_float_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRest_of_float_list" ):
                listener.enterRest_of_float_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRest_of_float_list" ):
                listener.exitRest_of_float_list(self)




    def rest_of_float_list(self):

        localctx = adder2Parser.Rest_of_float_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_rest_of_float_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.float_list()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Float_numContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._FLOAT = None # Token

        def FLOAT(self):
            return self.getToken(adder2Parser.FLOAT, 0)

        def getRuleIndex(self):
            return adder2Parser.RULE_float_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_num" ):
                listener.enterFloat_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_num" ):
                listener.exitFloat_num(self)




    def float_num(self):

        localctx = adder2Parser.Float_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_float_num)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            localctx._FLOAT = self.match(adder2Parser.FLOAT)
            localctx.value = float((None if localctx._FLOAT is None else localctx._FLOAT.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Integer_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_value = None
            self._integer = None # IntegerContext
            self._integer_list = None # Integer_listContext

        def integer(self):
            return self.getTypedRuleContext(adder2Parser.IntegerContext,0)


        def COMMA(self):
            return self.getToken(adder2Parser.COMMA, 0)

        def integer_list(self):
            return self.getTypedRuleContext(adder2Parser.Integer_listContext,0)


        def getRuleIndex(self):
            return adder2Parser.RULE_integer_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_list" ):
                listener.enterInteger_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_list" ):
                listener.exitInteger_list(self)




    def integer_list(self):

        localctx = adder2Parser.Integer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_integer_list)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 57
                localctx._integer = self.integer()
                localctx.list_value = localctx._integer.value
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                localctx._integer = self.integer()
                self.state = 61
                self.match(adder2Parser.COMMA)
                self.state = 62
                localctx._integer_list = self.integer_list()
                localctx.list_value = localctx._integer.value + localctx._integer_list.list_value
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntegerContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.value = None
            self._INTEGER = None # Token

        def INTEGER(self):
            return self.getToken(adder2Parser.INTEGER, 0)

        def getRuleIndex(self):
            return adder2Parser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = adder2Parser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            localctx._INTEGER = self.match(adder2Parser.INTEGER)
            localctx.value = int((None if localctx._INTEGER is None else localctx._INTEGER.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





