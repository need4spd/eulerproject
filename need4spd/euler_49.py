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
import itertools
  
p=list()
permutations=list(itertools.permutations(list(range(1,10)),4))
for t in permutations:
    s="".join(str(n) for n in t)
    p.append(s)


prime_list = [int(n) for n in p if isPrime(n)]
prime_list.sort()

index = 0
while True:

  if index+3 >= len(prime_list):
    break
    
  temp_l = prime_list[index: index+3]
  
  a=temp_l[0]
  b=temp_l[1]
  c=temp_l[2]
  
  if b-a == c-a:
    print (a,b,c,d)
  
  index += 1
