# Generated from adder2.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,54,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,3,3,3,25,8,3,1,3,4,3,28,
        8,3,11,3,12,3,29,1,4,3,4,33,8,4,1,4,4,4,36,8,4,11,4,12,4,37,1,4,
        1,4,4,4,42,8,4,11,4,12,4,43,3,4,46,8,4,1,5,4,5,49,8,5,11,5,12,5,
        50,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,9,5,11,6,1,0,5,2,0,65,65,97,97,
        2,0,68,68,100,100,2,0,86,86,118,118,2,0,69,69,101,101,3,0,9,10,13,
        13,32,32,60,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,1,13,1,0,0,0,3,17,1,0,0,0,5,21,1,0,0,0,7,24,
        1,0,0,0,9,32,1,0,0,0,11,48,1,0,0,0,13,14,7,0,0,0,14,15,7,1,0,0,15,
        16,7,1,0,0,16,2,1,0,0,0,17,18,7,0,0,0,18,19,7,2,0,0,19,20,7,3,0,
        0,20,4,1,0,0,0,21,22,5,44,0,0,22,6,1,0,0,0,23,25,5,45,0,0,24,23,
        1,0,0,0,24,25,1,0,0,0,25,27,1,0,0,0,26,28,2,48,57,0,27,26,1,0,0,
        0,28,29,1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,8,1,0,0,0,31,33,5,
        45,0,0,32,31,1,0,0,0,32,33,1,0,0,0,33,35,1,0,0,0,34,36,2,48,57,0,
        35,34,1,0,0,0,36,37,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,45,1,
        0,0,0,39,41,5,46,0,0,40,42,2,48,57,0,41,40,1,0,0,0,42,43,1,0,0,0,
        43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,45,39,1,0,0,0,45,46,1,
        0,0,0,46,10,1,0,0,0,47,49,7,4,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,
        48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,53,6,5,0,0,53,12,1,0,0,
        0,8,0,24,29,32,37,43,45,50,1,0,1,0
    ]

class adder2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ADD = 1
    AVE = 2
    COMMA = 3
    INTEGER = 4
    FLOAT = 5
    WS = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','" ]

    symbolicNames = [ "<INVALID>",
            "ADD", "AVE", "COMMA", "INTEGER", "FLOAT", "WS" ]

    ruleNames = [ "ADD", "AVE", "COMMA", "INTEGER", "FLOAT", "WS" ]

    grammarFileName = "adder2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


