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


def getQuadrant(x, y):
  """
  This functions have 2 parameters, x and y (-10^9 <= x, y <= 10^9) and returns the quadrant where the (x, y) is located.
  """
  if x > 0 and y > 0:
    return 1
  elif x < 0 and y > 0:
    return 2
  elif x < 0 and y < 0:
    return 3
  else:
    return 4

def binExpMOD(b, p):
  """
  This function have 2 parameters, b and p, and return (b^p)%MOD.
  """
  global MOD
  ans = None
  if p == 0:
    ans = 1
  elif p%2 == 0:
    ans = binExpMOD(b, p//2)%MOD
    ans = (ans*ans)%MOD
  else:
    ans = ((b%MOD)*(binExpMOD(b, p-1))%MOD)%MOD
  return ans

def C(n, k):
  global factorial, inverse, MOD
  ans = None
  if k == 0 or k == n:
    ans = 1
  else:
    ans = (factorial[n] * inverse[ (factorial[k]*factorial[n-k])%MOD  ]%MOD)%MOD
  return ans

# def solve(quadrants):
#   ##

## Initializing factorial and inverse arrays
factorial = [1 for _ in range(100001)]

for i in range(1, 100001):
  factorial[i] = (factorial[i-1]*(i%MOD))%MOD

inverse = [0 for _ in range(MOD)]
inverse[1] = 1

for i in range(2, MOD):
  inverse[i] = binExpMOD(i, MOD-2)
  #inverse[i] = ((MOD-(MOD//i))*inverse[MOD%i])%MOD

def main():
  global MOD, factorial, inverse
  lines = stdin.readlines()
  i = 1

  while i < len(lines):
    n = int(lines[i].strip())
    i += 1

    ##Quadrants array
    quadrants = [0 for _ in range(4)]

    for j in range(n):
      x, y = map(int, lines[i].strip().split())
      quadrants[getQuadrant(x, y)-1] += 1
      i += 1

#main()