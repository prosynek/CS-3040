--
-- Course: CS3040 - 021
-- Fall 2022
-- Exercise 6 - Bottom Up Evaluator
-- Name: Paige Rosynek
-- Date: 10.26.2022
--
-- NOTE : I worked with a group to complete this as allowed by project guidelines


--
-- bottom-up-eval.hs: construct bottom up parse with an evaluation operation
--   at each reduce step
--
-- This is a partial implementation; it is an exercise to complete it.
--
module BottomUpEval where

import Data.List -- for find operation
import Debug.Trace

type Grammar = [Rule]
type Rule = (Nonterminal, [GSymbol], Action)
data GSymbol = T Terminal | N Nonterminal
               deriving (Eq, Show)
type Label = String
type Terminal = Char
type Nonterminal = String
type Action = [Int] -> Int
type MatchStack = [(GSymbol, Int)] -- stack of symbols and the computed value for each symbol

simpleBinaryNumberGrammar :: Grammar
simpleBinaryNumberGrammar = [
  ("number", [N "bits"], \x -> (head x)),
  ("bits", [N "bit"], \x -> (head x)),
  ("bits", [N "bits", N "bit"], \x -> (2 * (x !! 0) + (x !! 1))),  
  ("bit", [T '0'], \x -> 0),
  ("bit", [T '1'], \x -> 1)
 ]


exprGrammar :: Grammar
exprGrammar = [
  ("Expression", [N "Term"], \x -> (head x)),
  ("Expression", [N "Term", T '+', N "Expression"], \x -> ((x !! 0) + (x !! 2))),  
  ("Term", [N "Factor"], \x -> (head x)),
  ("Term", [N "Factor", T '*', N "Term"], \x -> ((x !! 0) * (x !! 2))), 
  ("Factor", [N "Number"], \x -> (head x)),
  ("Factor", [T '(', N "Expression", T ')'], \x -> (x !! 1)), 
  ("Number", [T '0'], \x -> 0),
  ("Number", [T '1'], \x -> 1),
  ("Number", [T '2'], \x -> 2),
  ("Number", [T '3'], \x -> 3),
  ("Number", [T '4'], \x -> 4),
  ("Number", [T '5'], \x -> 5),
  ("Number", [T '6'], \x -> 6),
  ("Number", [T '7'], \x -> 7),
  ("Number", [T '8'], \x -> 8),
  ("Number", [T '9'], \x -> 9)
  ]


-- eval: given a grammar and a string, returns -1 if the string is invalid
--       and the value computed by the actions otherwise
eval :: Grammar -> String -> Int
eval grammar input = steps grammar [] input -- Begin with empty stack

-- equivalent of or but for numbers: return first argument if non-negative,
--    otherwise return the second
non_negative_or :: Int -> Int -> Int
non_negative_or x y | x < 0 = y
non_negative_or x _ = x

-- return first nonnegative value from a list or -1 if all values negative
first_non_negative :: [Int] -> Int
first_non_negative [] = -1
first_non_negative (x:xs) | x >= 0 = x
first_non_negative (_:xs) = first_non_negative xs

-- steps: apply shift & reduce until reach end of input, returning >= 0 on
--        success and <0 on failure
steps :: Grammar -> MatchStack -> String -> Int

-- Acceptance succeeds (start symbol on stack, all input consumed)
steps grammar [(N nonterminal, val)] [] | nonterminal == start_nonterminal = val
  where
    -- Retrieve start symbol
    ((start_nonterminal, _, _):_) = grammar

steps grammar to_match input = non_negative_or shift_result reduce_result
  where

    -- Shift terminal from input to stack, setting value to 0
    shift_result =
        if null input
        then -1
        else steps grammar ((T (head input), 0) : to_match) (tail input)


    -- the right hand side of the production
    reduce_result =
        if null match_stacks
        then -1
        else first_non_negative (map (\to_match -> steps grammar to_match input)
                                match_stacks)
      where
        -- Retrieve relevant reductions and apply the Action to the associated values
        match_stacks = [ (N n, (apply_action e (take rhs_len to_match))) : drop rhs_len to_match
                         | (n, rhs, e) <- grammar,
                           let rhs_len = length rhs,
                           (production_rhs_at_top rhs (take rhs_len to_match))
                       ]

-- return true if top of matchstack matches rhs
-- Note that the symbols will be in reverse order on the stack
-- Example: production_rhs_at_top [N "a", T "b"] [(T "b", 5), (N "a", 6)]
--   would return true; pseudocode: take the top elements, reverse them, and match to rhs
production_rhs_at_top :: [GSymbol] -> MatchStack -> Bool
production_rhs_at_top rhs candidate_items = if [symbol | (symbol, num) <- reverse candidate_items] == rhs then True else False

-- for example: if e is (\x -> sum x) and stack_elements is [(N a, 19), (N b, 6)] (assuming a production
--    Something -> A B), then you would compute the list [19, 6] (the second element from each pair)
--    and apply e to that list (in this case, \x -> sum x), giving the result of 25
-- Note: given fun = \x -> 3 * (x !! 0) + 4 * (x !! 1), then (fun [2, 3]) gives 18
-- Hint: the elements on the match stack will be in reverse order from the production,
--    so you'll probably want to reverse this list before applying the action.
apply_action :: Action -> MatchStack -> Int
apply_action action stack_elements =  action [num | (symbol, num) <- reverse stack_elements]

-- :load BottomUpEval.hs
-- eval simpleBinaryNumberGrammar "1"
-- eval exprGrammar "3*(1+5*2+3)"