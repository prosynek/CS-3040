grammar adder2;

/* 
 * Sample ANTLR file that illustrates computing results in a simple case.
 */

commands
   : addCommand+ EOF
   | aveCommand+ EOF
   ;

addCommand
   : ADD integer_list
        {print("Sum: " + str($integer_list.list_value))}
   ;

aveCommand
   : AVE float_list
         {print($float_list.list)}
         {print("Average: " + str(sum($float_list.list) / len($float_list.list)))}
   ;

float_list returns [list]
   : float_num
      {$list = [$float_num.value]}
   | float_num COMMA rest_of_float_list
      {$list.append($float_num.value)}
   ;

rest_of_float_list returns [list]
   : float_list
      {}
   ;

float_num returns [float value]
   : FLOAT
      {$value = float($FLOAT.text)}
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

AVE
   : ('a'|'A')('v'|'V')('e'|'E')
   ;

COMMA
   : ','
   ;

INTEGER
   : '-'? ('0'..'9')+
   ;

FLOAT
   : '-'?('0'..'9')+('.'('0'..'9')+)?
   ;

WS
   : [ \r\n\t]+ -> channel (HIDDEN)
   ;
