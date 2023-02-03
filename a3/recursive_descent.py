"""
- CS3040 - 001
- Fall 2022
- Assignment 3 - Recursive Descent Parser
- Name: Paige Rosynek
- Date: 11.3.2022
"""

from sys import stdin
import re


class Tokenizer:
    """
    Class to separate input into tokens and to move through each input token
    """
    def __init__(self, words):
        """
        Constructor to create Tokenizer object
        
        :param str words: the input string to be tokenized
        """
        self.valid_punc = ['[', ']', ',', '{', '}']
        self.index = -1
        self.tokens = self._tokenize(words)
            
        
    def _tokenize(self, words):
        """
        Splits input string into tokens
        
        :param str words: the input string to be tokenized
        """
        formatted = self._format_punc(words)
        tokens = formatted.split()
        tokens.append('$')  # tacks on $ character to signal end of input tokens
        return tokens
       
            
    def _format_punc(self, words):
        """
        Formats the valid punctuation in the input string so they can be split into separate tokens
        
        :param str words: the input string to be tokenized
        """
        for c in self.valid_punc:
            spaced = ' ' + c + ' '
            words = words.replace(c, spaced)
            
        return words
    

    def next_token(self):
        """
        Returns the next token in the token list
        
        :return: the next token
        :rtype: str
        """
        return self.tokens[self.index + 1]

    
    def at_end(self):
        """
        Checks if the current position is at the end of the token list
        
        :return: True if the current position is at the end, otherwise False
        :rtype: Bool
        """
        return self.next_token() == '$'                                 
    
    
    def advance(self):
        """
        Advances the current position (index) by one
        """
        if not self.at_end():
            self.index += 1
            

    def expect(self, e):
        """
        Checks if the next token in the token list is the expected token.
        If True, advance the current index by one (next token).
        
        :param char e: expected token to be at the current index
        :raises Exception: if the expected token is not the next token
        """
        if self.at_end():
            raise Exception(f'Syntax error in plan: no more tokens, but expected {e}')
        
        if self.next_token() == e:
            self.advance()
        else:
            raise Exception(f'Syntax error in plan: Expected {e}, received {self.next_token()}') # Syntax error in plan
                    
            
    def fail(self):
        """
        Exits program on parse failure
        """
        exit()



class DescentParser:
    """
    Recursive descent parser that parses the given building grammar.
    Then calculates and outputs the area of the complex for valid input.
    """
    def __init__(self, tokenizer):
        """
        Constructor to create a DescentParser object
        
        :param Tokenizer tokenizer: tokenizer to keep track of input tokens
        """
        self.tokenizer = tokenizer
        self.buildings = {}         # {BUILDING NAME : [floor1, floor2, ...], ...}
        self.floors = {}            # {FLOOR NAME : [(length, width),...], ...}
        
        
    def parse(self):
        """
        Parses input string using recursive descent
        """
        if self.tokenizer.at_end():
            print('Input cannot be empty')
            self.tokenizer.fail()
        
        try:
            self._parse_plans()
            self.output_complex_area()
        except Exception as e:
            print(e)
            self.tokenizer.fail()
            
    
    
    def _parse_plans(self):
        """
        Parses 'Plan' production rule
        
        :raises Exception: if not all tokens are read, or if expected token does not match
        """
        if self.tokenizer.next_token() != 'floor':
            raise Exception(f'Syntax error in plan: Expected floor, received {self.tokenizer.next_token()}')
        
        while self.tokenizer.next_token() == 'floor':
            self._parse_floor()     
            
        self._parse_complex()
        
        if not self.tokenizer.at_end():
            raise Exception('end of input expected')
        

    def _parse_floor(self):
        """
        Parses 'Floor' production rule
        """
        self.tokenizer.expect('floor')
        
        floor_name = self._parse_name()
        
        # check for duplicate floors
        if floor_name in self.floors.keys():
            raise Exception(f'Duplicate floor {floor_name}')
            self.tokenizer.fail()
        
        self.tokenizer.expect('has')
        
        if self.tokenizer.next_token() == 'rooms' or self.tokenizer.next_token() == 'room':
            self.tokenizer.advance()
            rooms = self._parse_room_list()
            self.floors[floor_name] = rooms
        else:
            self.tokenizer.fail()

        
    def _parse_complex(self):
        """
        Parses 'Complex' production rule
        """
        self.tokenizer.expect('complex')
        
        while self.tokenizer.next_token() == 'building':
            self._parse_building()
        
    
    def _parse_building(self):
        """
        Parses 'Building' production rule
        """
        self.tokenizer.expect('building')
        building_name = self._parse_name()
        
        self.tokenizer.expect('with')
        
        if self.tokenizer.next_token() == 'floor' or self.tokenizer.next_token() == 'floors':
            self.tokenizer.advance()
            floors = self._parse_floor_list() 
            self.buildings[building_name] = floors 
        else:
            self.tokenizer.fail()
    
    
    def _parse_floor_list(self):
        """
        Parses 'FloorList' production rule

        :return: list containing the floor names for the building
        :rtype: list of str
        """
        building = []
        
        self.tokenizer.expect('{')
        floor_name = self._parse_floor_reference()
        
        # checks if floor name is in the list of specified floors
        try:
            self.check_valid_floor(floor_name)
            building.append(floor_name)
        except Exception as e:
            print(e)
            self.tokenizer.fail()
        
        while self.tokenizer.next_token() == ',':
            self.tokenizer.advance()
            floor = self._parse_floor_reference()
            try:
                self.check_valid_floor(floor)
                building.append(floor)
            except Exception as e:
                print(e)
                self.tokenizer.fail()
        
        self.tokenizer.expect('}')
    
        return building
        
    
    def _parse_floor_reference(self):
        """
        Parses 'FloorReference' production rule

        :return: floor name
        :rtype: str
        """
        return self._parse_name()
    
    
    def _parse_room_list(self):
        """
        Parses 'RoomList' production rule

        :return: list representing the dimensions of each room
        :rtype: list of tuples
        """
        room_dimensions = []        
        
        self.tokenizer.expect('[')
        room = self._parse_room() 
        
        room_dimensions.append(room)
        
        while self.tokenizer.next_token() == ',':
            self.tokenizer.advance()
            r = self._parse_room()
            room_dimensions.append(r)
            
        self.tokenizer.expect(']')
        
        return room_dimensions
        
    
    def _parse_room(self):
        """
        Parses 'Room' production rule
        
        :return: room dimensions
        :rtype: tuple of str
        """
        l = self._parse_number()
        self.tokenizer.expect('by')
        w = self._parse_number()
        return (l, w)
    
    
    def _parse_name(self):
        """
        Parses 'Name' production rule
        
        :return: parsed name
        :rtype: str
        :raises Exception: if token does not match the pattern [A-Z_]+
        """
        if re.match('[A-Z_]+', self.tokenizer.next_token()):
            name = self.tokenizer.next_token()
            self.tokenizer.advance()
            return name
        else:
            raise Exception(f'Invalid name : {self.tokenizer.next_token()}')
    
    
    def _parse_number(self):
        """
        Parses 'Number' production rule
        
        :return: parsed number
        :rtype: str
        :raises Exception: if token does not match the pattern [0-9]+
        """
        if re.match('[0-9]+', self.tokenizer.next_token()):
            num = self.tokenizer.next_token()
            self.tokenizer.advance()
            return num
        else:
            raise Exception(f'Invalid number : {self.tokenizer.next_token()}')


    def check_valid_floor(self, floor):
        """
        Checks if floor specified in builing exists in the list of floors
        
        :param str floor: floor name to check
        :raises Exception: if floor does not exist in the list of floors
        """
        if floor not in list(self.floors.keys()):
            raise Exception(f'Reference to missing floor {floor}')
        
        
    def output_complex_area(self):
        """
        Calculates and outputs the area of each building and the total area of the complex for a valid input string
        """
        total_area = 0
        for building, floor_list in self.buildings.items():
            area = 0
            for floor in floor_list:
                rooms = self.floors[floor] 
                area += sum(map(lambda room: int(room[0]) * int(room[1]), rooms))
                
            total_area += area
            print(f'Area for building {building}: {area} square feet.')
        
        print(f'Total area: {total_area} square feet.')
        
    
    
if __name__ == '__main__':
    input = stdin.read()
    
    try:
        tokenizer = Tokenizer(input)
        parser = DescentParser(tokenizer)
        parser.parse()
        
    except Exception as e:
        print(e)