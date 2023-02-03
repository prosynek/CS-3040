# Generated from adder.g4 by ANTLR 4.11.1
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
        4,1,6,69,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,0,4,0,23,8,0,11,0,12,0,24,
        1,0,1,0,3,0,29,8,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,3,3,48,8,3,1,4,1,4,1,4,1,4,3,4,54,8,4,1,5,
        1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,64,8,5,1,6,1,6,1,6,1,6,0,0,7,0,2,
        4,6,8,10,12,0,0,67,0,28,1,0,0,0,2,30,1,0,0,0,4,34,1,0,0,0,6,47,1,
        0,0,0,8,53,1,0,0,0,10,63,1,0,0,0,12,65,1,0,0,0,14,16,3,2,1,0,15,
        14,1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,
        0,19,20,5,0,0,1,20,29,1,0,0,0,21,23,3,4,2,0,22,21,1,0,0,0,23,24,
        1,0,0,0,24,22,1,0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,27,5,0,0,1,
        27,29,1,0,0,0,28,15,1,0,0,0,28,22,1,0,0,0,29,1,1,0,0,0,30,31,5,1,
        0,0,31,32,3,10,5,0,32,33,6,1,-1,0,33,3,1,0,0,0,34,35,5,2,0,0,35,
        36,3,6,3,0,36,37,6,2,-1,0,37,5,1,0,0,0,38,39,3,8,4,0,39,40,6,3,-1,
        0,40,48,1,0,0,0,41,42,3,8,4,0,42,43,5,3,0,0,43,44,3,6,3,0,44,45,
        6,3,-1,0,45,46,6,3,-1,0,46,48,1,0,0,0,47,38,1,0,0,0,47,41,1,0,0,
        0,48,7,1,0,0,0,49,50,5,5,0,0,50,54,6,4,-1,0,51,52,5,4,0,0,52,54,
        6,4,-1,0,53,49,1,0,0,0,53,51,1,0,0,0,54,9,1,0,0,0,55,56,3,12,6,0,
        56,57,6,5,-1,0,57,64,1,0,0,0,58,59,3,12,6,0,59,60,5,3,0,0,60,61,
        3,10,5,0,61,62,6,5,-1,0,62,64,1,0,0,0,63,55,1,0,0,0,63,58,1,0,0,
        0,64,11,1,0,0,0,65,66,5,4,0,0,66,67,6,6,-1,0,67,13,1,0,0,0,6,17,
        24,28,47,53,63
    ]

class adderParser ( Parser ):

    grammarFileName = "adder.g4"

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
    RULE_float_num = 4
    RULE_integer_list = 5
    RULE_integer = 6

    ruleNames =  [ "commands", "addCommand", "aveCommand", "float_list", 
                   "float_num", "integer_list", "integer" ]

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
            return self.getToken(adderParser.EOF, 0)

        def addCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(adderParser.AddCommandContext)
            else:
                return self.getTypedRuleContext(adderParser.AddCommandContext,i)


        def aveCommand(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(adderParser.AveCommandContext)
            else:
                return self.getTypedRuleContext(adderParser.AveCommandContext,i)


        def getRuleIndex(self):
            return adderParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)




    def commands(self):

        localctx = adderParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_commands)
        self._la = 0 # Token type
        try:
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 14
                    self.addCommand()
                    self.state = 17 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==1):
                        break

                self.state = 19
                self.match(adderParser.EOF)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 21
                    self.aveCommand()
                    self.state = 24 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break

                self.state = 26
                self.match(adderParser.EOF)
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
            return self.getToken(adderParser.ADD, 0)

        def integer_list(self):
            return self.getTypedRuleContext(adderParser.Integer_listContext,0)


        def getRuleIndex(self):
            return adderParser.RULE_addCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddCommand" ):
                listener.enterAddCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddCommand" ):
                listener.exitAddCommand(self)




    def addCommand(self):

        localctx = adderParser.AddCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_addCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(adderParser.ADD)
            self.state = 31
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
            return self.getToken(adderParser.AVE, 0)

        def float_list(self):
            return self.getTypedRuleContext(adderParser.Float_listContext,0)


        def getRuleIndex(self):
            return adderParser.RULE_aveCommand

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAveCommand" ):
                listener.enterAveCommand(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAveCommand" ):
                listener.exitAveCommand(self)




    def aveCommand(self):

        localctx = adderParser.AveCommandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_aveCommand)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(adderParser.AVE)
            self.state = 35
            localctx._float_list = self.float_list()
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
            self._float_list = None # Float_listContext

        def float_num(self):
            return self.getTypedRuleContext(adderParser.Float_numContext,0)


        def COMMA(self):
            return self.getToken(adderParser.COMMA, 0)

        def float_list(self):
            return self.getTypedRuleContext(adderParser.Float_listContext,0)


        def getRuleIndex(self):
            return adderParser.RULE_float_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_list" ):
                listener.enterFloat_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_list" ):
                listener.exitFloat_list(self)




    def float_list(self):

        localctx = adderParser.Float_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_float_list)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                localctx._float_num = self.float_num()
                localctx.list_ = [localctx._float_num.value]
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 41
                localctx._float_num = self.float_num()
                self.state = 42
                self.match(adderParser.COMMA)
                self.state = 43
                localctx._float_list = self.float_list()
                localctx.list_ = localctx._float_list.list_
                (localctx.list_).append(localctx._float_num.value)
                pass


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
            self._INTEGER = None # Token

        def FLOAT(self):
            return self.getToken(adderParser.FLOAT, 0)

        def INTEGER(self):
            return self.getToken(adderParser.INTEGER, 0)

        def getRuleIndex(self):
            return adderParser.RULE_float_num

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFloat_num" ):
                listener.enterFloat_num(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFloat_num" ):
                listener.exitFloat_num(self)




    def float_num(self):

        localctx = adderParser.Float_numContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_float_num)
        try:
            self.state = 53
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                localctx._FLOAT = self.match(adderParser.FLOAT)
                localctx.value = float((None if localctx._FLOAT is None else localctx._FLOAT.text))
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                localctx._INTEGER = self.match(adderParser.INTEGER)
                localctx.value = float((None if localctx._INTEGER is None else localctx._INTEGER.text))
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


    class Integer_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.list_value = None
            self._integer = None # IntegerContext
            self._integer_list = None # Integer_listContext

        def integer(self):
            return self.getTypedRuleContext(adderParser.IntegerContext,0)


        def COMMA(self):
            return self.getToken(adderParser.COMMA, 0)

        def integer_list(self):
            return self.getTypedRuleContext(adderParser.Integer_listContext,0)


        def getRuleIndex(self):
            return adderParser.RULE_integer_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger_list" ):
                listener.enterInteger_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger_list" ):
                listener.exitInteger_list(self)




    def integer_list(self):

        localctx = adderParser.Integer_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_integer_list)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 55
                localctx._integer = self.integer()
                localctx.list_value = localctx._integer.value
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 58
                localctx._integer = self.integer()
                self.state = 59
                self.match(adderParser.COMMA)
                self.state = 60
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
            return self.getToken(adderParser.INTEGER, 0)

        def getRuleIndex(self):
            return adderParser.RULE_integer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInteger" ):
                listener.enterInteger(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInteger" ):
                listener.exitInteger(self)




    def integer(self):

        localctx = adderParser.IntegerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_integer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            localctx._INTEGER = self.match(adderParser.INTEGER)
            localctx.value = int((None if localctx._INTEGER is None else localctx._INTEGER.text))
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





