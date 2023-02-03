grammar plan;

@header {
buildings = {}
floors = {}
}

plan
    : (floor)+ complex EOF
    ;

floor
    : FLOOR name HAS ROOMS room_list
        {print(f'room list = {$room_list.dimension_list}')}
    | FLOOR name HAS ROOM room_list
    ;

complex
    : COMPLEX (building)+
    ;

building
    : BUILDING name WITH FLOORS floor_list
    | BUILDING name WITH FLOOR floor_list
    ;

floor_list returns [floors]
    : LCBRACKET floor_reference 
        {$floors = [$floor_reference.floor_name]}
    more_floors RCBRACKET
        {$floors = $floors + $more_floors.floors}
    ;

more_floors returns [floors]
    : COMMA floor_reference 
        {$floors = [$floor_reference.floor_name]}
    more_floors
        {$floors = $floors + $more_floors.floors}
    | EMPTY
        {$floors = $floors + []}
    ;

floor_reference returns [floor_name]
    : name
        {$floor_name = $name.value}
    ;

room_list returns [dimension_list]
    : LBRACKET room
        {$dimension_list = [$room.dimensions]}
    more_rooms RBRACKET
        {print('room : ', $room.dimensions)}
        {$dimension_list = $dimension_list + $more_rooms.dimension_list}
        {print(f'dimension_list = {$dimension_list}')}
        {print('room : ', $room.dimensions)}
    ;

more_rooms returns [dimension_list]
    : COMMA room 
        {$dimension_list = [$room.dimensions]}
    more_rooms
        {$dimension_list = $dimension_list + $more_rooms.dimension_list}
    | EMPTY
        {$dimension_list = $dimension_list + []}
    ;

room returns [dimensions]   
    : number 
        {$dimensions = [$number.value]}
    BY number
        {$dimensions.append($number.value)}
        {print(f'dimensions = {$dimensions}')}
    ;

name returns [value]
    : NAME
        {$value = $NAME.text}
    ;

number returns [value]
    : NUMBER
        {$value = int($NUMBER.text)}
    ;

COMMA
    : ','
    ;

LCBRACKET
    : '{'
    ;

RCBRACKET
    : '}'
    ;

LBRACKET
    : '['
    ;

RBRACKET
    : ']'
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

EMPTY
    :
    ;

WS
   : [ \r\n\t]+ -> channel (HIDDEN)
   ;