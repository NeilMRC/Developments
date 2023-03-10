from sympy import *


def solveforx(eq):
  # Identify all variables
  #var('a b c d x') 
  x = symbols('x')

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


def derivative(eq2):
  x = symbols('x')
  sol = diff(eq2,x)
  return sol

def integration(eq3):
  x, y = symbols('x y')
  sol = integrate(eq3,x)
  return sol