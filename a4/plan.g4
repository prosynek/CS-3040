grammar plan;

@header {
"""
- CS3040 - 001
- Fall 2022
- Assignment 4 - Complex ANTLRs
- Name: Paige Rosynek
- Date: 11.10.2022
"""
buildings = {}
floors = {}

def check_valid_floor(floor):
        """
        Checks if floor specified in builing exists in the list of floors
        
        :param str floor: floor name to check
        :raises Exception: if floor does not exist in the list of floors
        """
        if floor not in list(floors.keys()):
            raise Exception(f'Reference to missing floor {floor}')


def check_duplicate_floor(floor):
    """
        Checks if floor is already specified in the list of floors
        
        :param str floor: floor name to check
        :raises Exception: if floor exists in the list of floors
    """
    if floor in floors.keys():
        raise Exception(f'Duplicate floor {floor}')
        

def output_complex_area():
    """
    Calculates and outputs the area of each building and the total area of the complex for a valid input string
    """
    total_area = 0
    for building, floor_list in buildings.items():
        area = 0
        for floor in floor_list:
            rooms = floors[floor] 
            area += sum(map(lambda room: int(room[0]) * int(room[1]), rooms))
            
        total_area += area
        print(f'Area for building {building}: {area} square feet.')
    
    print(f'Total area: {total_area} square feet.')
}

plan
    : (floor)+ complex EOF
        {output_complex_area()}
    ;

floor
    : FLOOR name HAS ROOMS room_list
        {try:}
        {   check_duplicate_floor($name.value)}
        {   floors[$name.value] = $room_list.dimension_list}
        {except Exception as e:}
        {   print(e)}
        {   exit()}
    | FLOOR name HAS ROOM room_list
        {try:}
        {   check_duplicate_floor($name.value)}
        {   floors[$name.value] = $room_list.dimension_list}
        {except Exception as e:}
        {   print(e)}
        {   exit()}
    ;

complex
    : COMPLEX (building)+
    ;

building
    : BUILDING name WITH FLOORS floor_list
        {buildings[$name.value] = $floor_list.floors}
    | BUILDING name WITH FLOOR floor_list
        {buildings[$name.value] = $floor_list.floors}
    ;

floor_list returns [floors]
    : LCBRACKET floor_reference 
        {try:}
        {   check_valid_floor($floor_reference.floor_name)}
        {   $floors = [$floor_reference.floor_name]}
        {except Exception as e:}
        {   print(e)}
        {   exit()}
    more_floors RCBRACKET
        {$floors = $floors + $more_floors.floors}
    ;

more_floors returns [floors]
    : COMMA floor_reference 
        {try:}
        {   check_valid_floor($floor_reference.floor_name)}
        {   $floors = [$floor_reference.floor_name]}
        {except Exception as e:}
        {   print(e)}
        {   exit()}
    more_floors
        {$floors = $floors + $more_floors.floors}
    | empty
        {$floors = []}
    ;

floor_reference returns [floor_name]
    : name
        {$floor_name = $name.value}
    ;

room_list returns [dimension_list]
    : LBRACKET room
        {$dimension_list = [$room.dimensions]}
    more_rooms RBRACKET
        {$dimension_list = $dimension_list + $more_rooms.dimension_list}
    ;

more_rooms returns [dimension_list]
    : COMMA room 
        {$dimension_list = [$room.dimensions]}
    more_rooms
        {$dimension_list = $dimension_list + $more_rooms.dimension_list}
    | empty
        {$dimension_list = []}
    ;

room returns [dimensions]   
    : number 
        {$dimensions = [$number.value]}
    BY number
        {$dimensions.append($number.value)}
    ;

name returns [value]
    : NAME
        {$value = $NAME.text}
    ;

number returns [value]
    : NUMBER
        {$value = int($NUMBER.text)}
    ;

empty
    :
    ;

COMMA
    : ','
    ;

LCBRACKET
    : '{'
    ;

LBRACKET
    : '['
    ;

BUILDING
    : 'building'
    ;

COMPLEX
    : 'complex'
    ;

ROOMS
    : 'rooms'
    ;

ROOM
    : 'room'
    ;

FLOOR
    : 'floor'
    ;

FLOORS
    : 'floors'
    ;

HAS 
    : 'has'
    ;

BY
    : 'by'
    ;

WITH
    : 'with'
    ;

NAME
    : ('A'..'Z'|'_')+
    ;

NUMBER
    : ('0'..'9')+
    ;

RCBRACKET
    : '}'
    ;

RBRACKET
    : ']'
    ;

WS
   : [ \r\n\t]+ -> channel (HIDDEN)
   ;