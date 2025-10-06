#! /usr/bin/python3
"""
Checks Goldbach Conjecture in an interval,
by brute force.
It does not generate any certificate.
"""

import os, sys

def pr(p: int) -> bool:
  """
  Primality test, for p odd >= 3
  """
  k = 3
  while k <= p/k:
    if p%k == 0:
      return False
    k += 2
  return True

def gbn(n: int) -> bool:
  """
  Checks Goldbach Conjecture for n (assumed even >= 6).
  """
  p = 3
  while p <= n-p:
    if pr(p):
      if pr(n - p):
        return True
    p += 2
  return False

def gbab(a: int, b: int) -> bool:
  """
  Checks Goldbach Conjecture in interval [a, b] (assumed a even, 6 <= a <= b).
  """
  if b < 2**64-2:
    return os.system("bin/goldbach_conjecture "+str(a)+" "+str(b)) == 0;
  n = a
  while n <= b:
    if gbn(n) == False:
      return False
    n += 2
  return True

if __name__=="__main__":
  a = int(sys.argv[1])<<20
  if a == 0:
    a = 6
  b = int(sys.argv[2])<<20
  if a%2 == 1:
      a += 1
  os.system("gcc -o bin/goldbach_conjecture src/core/goldbach_conjecture.c -Os -w -DHAS64BIT")
  sys.exit(gbab(a, b) == False)

