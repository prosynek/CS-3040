import antlr4
from antlr4.InputStream import InputStream
from antlr4.FileStream import FileStream
from antlr4.error.ErrorStrategy import BailErrorStrategy
from antlr4.error.Errors import ParseCancellationException
from adderLexer import adderLexer
from adderParser import adderParser
import sys

def main():
    input_stream = None
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        print("Enter 'add' followed by a comma-separated list of integers:")
        input_stream = InputStream(sys.stdin.readline())
    lexer = adderLexer(input_stream)
    stream = antlr4.CommonTokenStream(lexer)
    parser = adderParser(stream)
    parser._errHandler = BailErrorStrategy()
    try:
        tree = parser.commands()
    except ParseCancellationException as err:
        if lexer.column > 0:
            print("Syntax error in input around line " + str(lexer.line) +
                  ", column " + str(lexer.column))
        else:
            print("Syntax error in input around line " + str(lexer.line))

if __name__ == '__main__':
    main()
