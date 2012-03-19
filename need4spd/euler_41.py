def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True  
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

# euler 24
import itertools

p=list()
for n in range(2,11):
    l=list(range(1,n))
    permutations=list(itertools.permutations(l,len(l)))
 
    for t in permutations:
        s="".join(str(n) for n in t)
        p.append(s)

p.sort()
result = 0

for n in p:

  if isPrime(n):
    if result < int(n):
      result = int(n)

print (result)