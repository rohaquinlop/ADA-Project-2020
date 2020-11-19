"""
Autor: Robin Hafid Quintero Lopez
Código de estudiante: 8943155
Código de honor:
  Como miembro de la comunidad académica de la Pontificia Universidad Javeriana Cali
  me comprometo a seguir los más altos estándares de integridad académica.
"""
from sys import stdin

MOD = 7340033
factorial = []
inverse = []

## Initializing factorial and inverse arrays

"""
This procedure precalculate the factorial for each value in the range of 0 to 10^5.
Complexity O(n).
"""
factorial = [1 for _ in range(100001)]

for i in range(1, 100001):
  factorial[i] = (factorial[i-1]*(i%MOD))%MOD

"""
This procedure precalculate the modular inverse modulo MOD for the values in the range of 0 and MOD-1.
This procedure is correcto due to:
the inverse[i] = ((MOD-(MOD//i))*inverse[MOD%i])%MOD. Only apply if i >= 2, if i = 1 then the inverse is equal to 1.
Complexity O(n).
"""

inverse = [0 for _ in range(100001)]
inverse[1] = 1

for i in range(2, 100001):
  inverse[i] = ((MOD-(MOD//i))*inverse[MOD%i])%MOD


def getQuadrant(x, y):
  """
  Given and x and y, this function returns the quadrant where this coordinates points to.
  The complexity is O(1).
  """
  if x > 0 and y > 0:
    return 1
  elif x < 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  else:
    return 4

def C(n, k):
  """
  Given an n and k, this function returns de Combinatorics of n between k.
  To make this optimal two arrays are used (factorial and inverse).
  factorial contains precalculated the factorial values in the range of 0 and 10^5 for each value.
  inverse contains precalculated the modular inverse modulo MOD for values in the range of 0 and MOD-1.

  The combinatorics equation is iqual to: n!/(k!*(n-k)!).
  But this also can be seen as: n! * ( k!*(n-k)! )^-1.

  Due that the result must be given modulo MOD then can be used the precalculated inverse.
  The complexity is O(1).
  """
  global factorial, inverse, MOD
  res = None
  if k == 0 or k == n:
    res = 1
  else:
    res = (factorial[n] * inverse[ (factorial[k]*factorial[n-k])%MOD ]%MOD)%MOD
  return res

def polynomial(x, y):
  """
  Given an x and y, this function returns an array which contains the coefficients of the polynomial that's being computed.
  Each value for the polynomial is computed in the way that res[i] = C(x, i)*C(y, i).
  Return the res array.
  
  Complexity O(n).
  """
  k = min(x, y)
  res = []

  i = 0
  while i <= k:
    res.append( (C(x, i)*C(y, i))%MOD )
    i += 1

  return res

def FFTBruteForce(A, B):
  """
  Given 2 arrays A, B returns the multiplication of both arrays (Polynomial).
  """
  res = [0 for _ in range(len(A)+len(B)-1)]

  for i in range(len(A)):
    for j in range(len(B)):
      res[i+j] += ((A[i]%MOD)*(B[j]%MOD))%MOD
  
  return res

def solve(quadrants, n):
  """
  Given a quadrants array, gives the answer.
  """
  global factorial, inverse, MOD
  out = ""

  res = FFTBruteForce(polynomial(quadrants[0], quadrants[2]), polynomial(quadrants[1], quadrants[3]))
  j = 1

  for i in range(n):
    if (i+1)%2 != 0 or ((i+1)%2 == 0 and j >= len(res)):
      out += "0"
    else:
      out += "{}".format(res[j])
      j += 1
    
    if i < n-1:
      out += " "
  out += "\n"
  return out

def main():
  lines = stdin.readlines()
  i = 1
  out = ""
  cases = 1

  while i < len(lines):
    n = int(lines[i].strip())
    i += 1

    ##Quadrants array
    quadrants = [0 for _ in range(4)]

    for j in range(n):
      x, y = map(int, lines[i].strip().split())
      quadrants[getQuadrant(x, y)-1] += 1
      i += 1
    
    out += "Case {}:\n".format(cases)
    out += solve(quadrants, n)
    cases += 1
  print(out.strip())

main()