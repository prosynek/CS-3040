#
# fsm.py: defines a class for deterministic finite state machines
#   with operations step and run the machine on a given input
#

from collections import defaultdict

class FsmlException(Exception):
    # Base class for all FSML exceptions
    pass

class FsmlDistinctIdsException(FsmlException):
    pass

class FsmlDeterminismException(FsmlException):
    pass

class Fsm():
    def __init__(self):
        self.states = defaultdict(list)
        self.finalStates = set()
        self.currentState = None
        self.initialState = None
        self.DEBUG = False

    def addState(self, id, isFinal = False):
        '''Add a named state to the list of valid states for the DFSM; state can be
        marked as final.  Returns the FSM to allow adding transitions and
        other states.
        '''
        #print("Adding state " + id)
        if not self.initialState:
            self.initialState = id
        self.currentState = id
        if id in self.states:
            raise FsmlDistinctIdsException
        self.states[id] = dict()
        if isFinal:
            self.finalStates.add(id)
        return self

    def addTransition(self, event, action, target):
        '''Add a transition on an event (typically a character to match) from the
        "current" state (the last one added) to target states. The target is a
        string naming a state. If the target state does not exist, it is added
        to the list of states. The target can also be None in which case it is
        a transition back to the source state. The event (a string) specifies
        an input on which the transition is taken. If action is specified,
        this is printed when taking the transition.
        '''
        #print("  Adding transition on " + event + " going to " + target)
        if event in self.states[self.currentState]: 
            # machine not deterministic
            raise FsmlDeterminismException;
        self.states[self.currentState][event] = \
            (action, self.currentState if target is None else target)
        return self

    def addTransitionRange(self, eventLow, eventHigh, action, target):
        '''Add transitions for a range of characters going from eventLow
        to eventHigh. Both the low and high must be a single character.
        Both the low and high values are included in the range. All events
        use the same action and target. See addTransition().'''
        transitionRange = range(ord(eventLow), ord(eventHigh) + 1)
        for trans in transitionRange:
            self.addTransition(chr(trans), action, target)
        return self
    
    def isFinalState(self, state):
        '''Is the named state a final state?'''
        return state in self.finalStates

    def start(self):
        '''Start executing the machine on an input sequence.'''
        self.currentState = self.initialState
        if self.DEBUG:
            print("Starting machine in state " + str(self.currentState))

    def step(self, symbol):
        '''Advance machine one step on symbol, returning any executed action and the
        new state. Returns [None, None] if there is no appropriate transition.'''
        possibleTransitions = self.states[self.currentState]
        if symbol not in possibleTransitions:
            return [None, None]
        (action, targetState) = possibleTransitions[symbol]
        if self.DEBUG:
            print("Taking step from " + str(self.currentState) + " to " +
                  str(targetState) + " on " + str(symbol))
        self.currentState = targetState
        return action, targetState

    def run(self, input):
        '''Execute the FSM on the given input sequence, returning a triple consisting
        of the sequence of states visited, any remaining input, and any
        actions executed. Generally the remaining input will be the empty list
        if the machine is successful. Client is responsible for checking
        currentState to see if it is a final state.
        '''
        self.start()
        statesVisited = [self.currentState]
        input = list(input)
        output = []
        while input:
            symbol = input[0]
            action, targetState = self.step(symbol)
            if targetState is None:
                return [statesVisited, input, output]
            statesVisited.append(targetState)
            if action is not None: output.append(action)
            input.pop(0)
        return [statesVisited, [], output]

    def runAndReport(self, input, debug):
        visited, remainingInput, output = self.run(input)
        if remainingInput or not self.isFinalState(self.currentState):
            print("Machine REJECTED input " + str(input))
        else:
            print("Machine accepted input " + str(input))
            print("   Final state: " + visited[-1])
        if remainingInput:
            print("   Unprocessed input: " + str(remainingInput))
        elif not self.isFinalState(self.currentState):
            print("   All input processed")
        if output:
            print("   Executed actions:  " + str(output))
        if debug: 
            print("   States reached:    " + str(visited))
