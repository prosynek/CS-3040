# turnstile.py: create turnstile, run tests
#               this illustrates using the fluent API to create DFSMs

from fsm import Fsm

turnstile = \
    Fsm() \
      .addState("locked", isFinal = True) \
        .addTransition("ticket", "collect", "unlocked") \
        .addTransition("pass", "alarm", "exception") \
      .addState("unlocked") \
        .addTransition("ticket", "eject", "unlocked") \
        .addTransition("pass", None, "locked") \
      .addState("exception") \
        .addTransition("ticket", "eject", "exception") \
        .addTransition("pass", None, "exception") \
        .addTransition("mute", None, "exception") \
        .addTransition("release", None, "locked")

def testTurnstile(test, debug):
    allTests = test == 0
    if test == 1 or allTests:
        print("1. sequence: ticket, pass, ticket, pass")
        turnstile.runAndReport(['ticket', 'pass', 'ticket', 'pass'], debug)
    if test == 2 or allTests:
        print("2. sequence: ticket, pass, ticket, ticket")
        turnstile.runAndReport(['ticket', 'pass', 'ticket', 'ticket'], debug)
    if test == 3 or allTests:
        print("3. sequence: ticket, pass, ticket, pass, pass, mute, release, ticket, pass")
        turnstile.runAndReport(['ticket', 'pass', 'ticket', 'pass', 'pass', 
                                'mute', 'release', 'ticket', 'pass'], debug)
    if test == 4 or allTests:
        print("4. sequence: pass, release, release")
        turnstile.runAndReport(['pass', 'release', 'release'], debug)

def runTests():
    testNumber = int(input("Enter test number (1-4, 0 for all): "))
    debugResponse = str(input("Debug (y/n) "))
    debug = debugResponse == "y" or debugResponse == "Y"
    testTurnstile(testNumber, debug)
    return 0

if __name__ == "__main__":
    exit(runTests())
