# numbers.py: recognize numeric constants

"""
 * Course: CS3040 - 021
 * Fall 2022
 * Assignment 1 - DFSM for Numeric Constants
 * Name: Paige Rosynek
 * Date: 9.24.2022
"""

import tarfile
from fsm import Fsm
from numbers_test import NumberTest

numbers = \
    Fsm() \
        .addState('start') \
            .addTransition('0', None, target='zero') \
            .addTransitionRange('1', '9', None, target='decimal') \
            .addTransition('.', None, target='decimalpoint') \
        .addState('decimalpoint') \
            .addTransitionRange('0', '9', None, target='float') \
        .addState('zero', isFinal=True) \
            .addTransition('x', None, target='hexadecimal') \
            .addTransition('.', None, target='decimalpoint') \
            .addTransitionRange('0', '7', None, target='octal') \
        .addState('hexadecimal', isFinal=True) \
            .addTransitionRange('0', '9', None, target='hexadecimal') \
            .addTransitionRange('a', 'f', None, target='hexadecimal') \
            .addTransitionRange('A', 'F', None, target='hexadecimal') \
        .addState('octal', isFinal=True) \
            .addTransitionRange('0', '7', None, target='octal') \
        .addState('decimal', isFinal=True) \
            .addTransitionRange('0', '9', None, target='decimal') \
            .addTransition('.', None, target='decimalpoint') \
        .addState('float', isFinal=True) \
            .addTransitionRange('0', '9', None, target='float')

def main():
    testNumber = int(input("Enter test number (1-4, 0 for all): "))
    debugResponse = str(input("Debug (y/n) "))
    debug = debugResponse == "y" or debugResponse == "Y"
    print("")
    NumberTest().run(testNumber, debug, numbers)
    return 0

if __name__ == "__main__":
    exit(main())
