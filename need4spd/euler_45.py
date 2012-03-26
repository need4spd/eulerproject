"""
import math
 
def is_pentagonal(n):
  n = abs(n)
  p = ( math.sqrt(1 + 24*n) + 1 ) / 6
  return p==int(p)
  
def is_hexagonal(n):
  n = abs(n)
  p = ( math.sqrt(8*n + 1) + 1) /4
  return p == int(p)
  
def is_triangular(n):
  n = abs(n)
  p = (math.sqrt(8*n+1) - 1) / 2
  return p == int(p)
  
n = 40756
while True:
  if is_pentagonal(n) and is_hexagonal(n) and is_triangular(n):
    print (n)
    break
  n += 1
"""
max_n = 100000
t_n_set = set([n*(n+1)/2 for n in range(max_n)])
p_n_set = set([n*(3*n-1)/2 for n in range(max_n) ])
h_n_set = set([n*(2*n-1) for n in range(max_n) ])

print (t_n_set.intersection(p_n_set).intersection(h_n_set)) 