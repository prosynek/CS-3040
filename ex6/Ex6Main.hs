
import BottomUpEval

testEval problem grammar input = do
  putStrLn ("Problem " ++ problem ++ " on input " ++ input ++ ": ")
  let result = (eval grammar input) in
    putStrLn ("    " ++ (show result))

testBinaryValues = do
  testEval "binary" simpleBinaryNumberGrammar "1"
  testEval "binary" simpleBinaryNumberGrammar "0"
  testEval "binary" simpleBinaryNumberGrammar "10"
  testEval "multidigit binary" simpleBinaryNumberGrammar "1101"
  testEval "multidigit binary" simpleBinaryNumberGrammar "10110"
  testEval "nonbinary" simpleBinaryNumberGrammar "-1"

testExpressions = do
  testEval "digit" exprGrammar "9"
  testEval "sum" exprGrammar "8+7"
  testEval "multiply" exprGrammar "6*5"
  testEval "mix" exprGrammar "1+2*7*8+4+5"
  testEval "parenthesized" exprGrammar "3*(1+5*2+3)*4"
  testEval "deeply nested" exprGrammar "2*(((1))+(2+(3)))"

main = do
  testBinaryValues
  putStrLn ""
  testExpressions

-- ghc --make Ex6Main.hs