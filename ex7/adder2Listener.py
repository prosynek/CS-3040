# Generated from adder2.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .adder2Parser import adder2Parser
else:
    from adder2Parser import adder2Parser

# This class defines a complete listener for a parse tree produced by adder2Parser.
class adder2Listener(ParseTreeListener):

    # Enter a parse tree produced by adder2Parser#commands.
    def enterCommands(self, ctx:adder2Parser.CommandsContext):
        pass

    # Exit a parse tree produced by adder2Parser#commands.
    def exitCommands(self, ctx:adder2Parser.CommandsContext):
        pass


    # Enter a parse tree produced by adder2Parser#addCommand.
    def enterAddCommand(self, ctx:adder2Parser.AddCommandContext):
        pass

    # Exit a parse tree produced by adder2Parser#addCommand.
    def exitAddCommand(self, ctx:adder2Parser.AddCommandContext):
        pass


    # Enter a parse tree produced by adder2Parser#aveCommand.
    def enterAveCommand(self, ctx:adder2Parser.AveCommandContext):
        pass

    # Exit a parse tree produced by adder2Parser#aveCommand.
    def exitAveCommand(self, ctx:adder2Parser.AveCommandContext):
        pass


    # Enter a parse tree produced by adder2Parser#float_list.
    def enterFloat_list(self, ctx:adder2Parser.Float_listContext):
        pass

    # Exit a parse tree produced by adder2Parser#float_list.
    def exitFloat_list(self, ctx:adder2Parser.Float_listContext):
        pass


    # Enter a parse tree produced by adder2Parser#rest_of_float_list.
    def enterRest_of_float_list(self, ctx:adder2Parser.Rest_of_float_listContext):
        pass

    # Exit a parse tree produced by adder2Parser#rest_of_float_list.
    def exitRest_of_float_list(self, ctx:adder2Parser.Rest_of_float_listContext):
        pass


    # Enter a parse tree produced by adder2Parser#float_num.
    def enterFloat_num(self, ctx:adder2Parser.Float_numContext):
        pass

    # Exit a parse tree produced by adder2Parser#float_num.
    def exitFloat_num(self, ctx:adder2Parser.Float_numContext):
        pass


    # Enter a parse tree produced by adder2Parser#integer_list.
    def enterInteger_list(self, ctx:adder2Parser.Integer_listContext):
        pass

    # Exit a parse tree produced by adder2Parser#integer_list.
    def exitInteger_list(self, ctx:adder2Parser.Integer_listContext):
        pass


    # Enter a parse tree produced by adder2Parser#integer.
    def enterInteger(self, ctx:adder2Parser.IntegerContext):
        pass

    # Exit a parse tree produced by adder2Parser#integer.
    def exitInteger(self, ctx:adder2Parser.IntegerContext):
        pass



del adder2Parser