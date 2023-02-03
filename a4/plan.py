"""
- CS3040 - 001
- Fall 2022
- Assignment 4 - Complex ANTLRs
- Name: Paige Rosynek
- Date: 11.10.2022
"""
import antlr4
from antlr4.InputStream import InputStream
from antlr4.FileStream import FileStream
from antlr4.error.ErrorStrategy import BailErrorStrategy
from antlr4.error.Errors import ParseCancellationException
from planLexer import planLexer
from planParser import planParser
import sys

def main():
    input_stream = None
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        print("Enter complex to parse:")
        text = sys.stdin.read()
        input_stream = InputStream(text)
        
    lexer = planLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = planParser(stream)
    parser._errHandler = BailErrorStrategy()
    try:
        tree = parser.plan()
    except ParseCancellationException as err:
        if lexer.column > 0:
            print("Syntax error in input around line " + str(lexer.line) +
                  ":\tUnexpected token : " + str(lexer.text))
        else:
            print("Syntax error in input around line " + str(lexer.line))

if __name__ == '__main__':
    main()
