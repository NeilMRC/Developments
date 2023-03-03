from sympy import *


#print(simpy.__builtins__)
var('a b c d x') 
equa = '2*x**2-3'

def solveforx(eq):
  # Identify all variables
  var('a b c d x') 
  #x = symbols('x')

  # Left and right sides of the equal sign
  left = 0
  right = eq

  # Variable to solve for
  variable = x

  # Sympy equation left = right
  eq1 = Eq(left,sympify(right)) 

  # Sympy solve for that variable
  sol = solve(eq1,variable) 
  return sol
sol=solveforx(equa)
print("Solution is:",sol)