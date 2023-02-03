/*
* CS3040 - 001
* Fall 2022
* Exercise 7 - A tiny ANTLR program
* Name: Paige Rosynek
* Date: 11.4.2022
*/
grammar adder;

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
         {print("Average: " + str(sum($float_list.list) / len($float_list.list)))}
   ;

float_list returns [list]
   : float_num
      {$list = [$float_num.value]}
   | float_num COMMA float_list
      {$list = $float_list.list}
      {($list).append($float_num.value)}
   ;

float_num returns [float value]
   : FLOAT
      {$value = float($FLOAT.text)}
   | INTEGER
      {$value = float($INTEGER.text)}
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
   : '-'?('0'..'9')+('.'('0'..'9')+)
   ;

WS
   : [ \r\n\t]+ -> channel (HIDDEN)
   ;
