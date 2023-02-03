# Generated from adder.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .adderParser import adderParser
else:
    from adderParser import adderParser

# This class defines a complete listener for a parse tree produced by adderParser.
class adderListener(ParseTreeListener):

    # Enter a parse tree produced by adderParser#commands.
    def enterCommands(self, ctx:adderParser.CommandsContext):
        pass

    # Exit a parse tree produced by adderParser#commands.
    def exitCommands(self, ctx:adderParser.CommandsContext):
        pass


    # Enter a parse tree produced by adderParser#addCommand.
    def enterAddCommand(self, ctx:adderParser.AddCommandContext):
        pass

    # Exit a parse tree produced by adderParser#addCommand.
    def exitAddCommand(self, ctx:adderParser.AddCommandContext):
        pass


    # Enter a parse tree produced by adderParser#aveCommand.
    def enterAveCommand(self, ctx:adderParser.AveCommandContext):
        pass

    # Exit a parse tree produced by adderParser#aveCommand.
    def exitAveCommand(self, ctx:adderParser.AveCommandContext):
        pass


    # Enter a parse tree produced by adderParser#float_list.
    def enterFloat_list(self, ctx:adderParser.Float_listContext):
        pass

    # Exit a parse tree produced by adderParser#float_list.
    def exitFloat_list(self, ctx:adderParser.Float_listContext):
        pass


    # Enter a parse tree produced by adderParser#float_num.
    def enterFloat_num(self, ctx:adderParser.Float_numContext):
        pass

    # Exit a parse tree produced by adderParser#float_num.
    def exitFloat_num(self, ctx:adderParser.Float_numContext):
        pass


    # Enter a parse tree produced by adderParser#integer_list.
    def enterInteger_list(self, ctx:adderParser.Integer_listContext):
        pass

    # Exit a parse tree produced by adderParser#integer_list.
    def exitInteger_list(self, ctx:adderParser.Integer_listContext):
        pass


    # Enter a parse tree produced by adderParser#integer.
    def enterInteger(self, ctx:adderParser.IntegerContext):
        pass

    # Exit a parse tree produced by adderParser#integer.
    def exitInteger(self, ctx:adderParser.IntegerContext):
        pass



del adderParser