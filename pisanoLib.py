from sympy import Matrix
from errors import *

originator = [0, 1]
ender = [1, 0]

# a, b => b, a+b
def fibonacci(a, b):
  return b, a+b

# a, b => (b)%m, (a+b)%m
def fibonacciMod(a, b, modulus):
  a, b = fibonacci(a, b)
  return a % modulus, b % modulus

# the Fibonacci numbers mod m from 0 to repitition
def pisanoList(m):
  array = originator

  a, b = fibonacciMod(*originator, m)

  while [a, b] != ender:
    array.append(b)
    a, b = fibonacciMod(a, b, m)

  return array

# m => π(m)
def pisanoPeriod(modulus):
  return len(pisanoList(modulus))

# return the 2D pisano array of modulus m and height h
def pisanoArray(modulus, height):
  if modulus < 3:
    raise InvalidModulusError(modulus)

  pList = pisanoList(modulus)
  period = len(pList)

  if period % height != 0:
      raise InvalidHeightError(height, period)
  
  array = []
  
  for i in range(height):
    column = []

    for j in range(int(period / height)):
      column.append(pList[height*j + i])
      
    array.append(column)

  return Matrix(array)
  