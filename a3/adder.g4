grammar adder;

/* 
 * Sample ANTLR file that illustrates computing results in a simple case.
 */

commands
   : addCommand+ EOF
   ;

addCommand
   : ADD integer_list
        {print("Sum: " + str($integer_list.list_value))}
   ;

integer_list returns [int list_value]
   : integer
        {$list_value = $integer.value}
   | integer COMMA integer_list
        {$list_value = $integer.value + $integer_list.list_value}
   ;

integer returns [int value]
   : INTEGER
        {$value = int($INTEGER.text)}
   ;

ADD
   : ('a'|'A')('d'|'D')('d'|'D')
   ;

COMMA
   : ','
   ;

INTEGER
   : '-'? ('0'..'9')+
   ;

WS
   : [ \r\n\t]+ -> channel (HIDDEN)
   ;
