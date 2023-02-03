{-
 - Course: CS3040 - 021
 - Fall 2022
 - Exercise 3 - Haskell Functions
 - Name: Paige Rosynek
 - Date: 10.1.2022
-}
module Ex3 where

{-
 - Function that implements the Ackermann Function
 - params : two integers
 - return : integer
-}
ack :: Integer -> Integer -> Integer
ack 0 n = n + 1
ack m 0 = ack (m - 1) 1
ack m n = ack (m - 1) (ack m (n - 1))


{-
 - Takes a list of items & returns a pair containing the 1st & 2nd elements
 - params : list of items
 - return : list of first two elements
-}
first_two :: [a] -> (a, a)
first_two n = (head n, head (tail n))


{-
 - Takes a list of numbers & returns the first even number
 - params : list of integers
 - return : integer of the first even number
-}
first_even :: [Integer] -> Integer
first_even x = if even (head x) then head x else first_even (tail x)

{-
 - Takes a list of items & swaps every other pair
 - params : list of items
 - return : list with every other item swapped
-}
swapPairs :: [a] -> [a]
swapPairs [] = []
swapPairs [x] = [x]
swapPairs (x:y:rest) = y:x:(swapPairs rest)