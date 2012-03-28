def isPrime(N):
    if N <= 1: return False
    if N == 2: return True
    if N % 2 == 0: return False
    for i in range(3, int(N**0.5)+1, 2):
        if N % i == 0: return False
    return True

def factorize(NUM):
    START = 2
    factors = []
    while NUM > 1:
      for num in range(START, NUM+1):
          if NUM % num == 0 and isPrime(num):
              NUM = int(NUM / num)
              factors.append(num)
              break
      START = num
    return factors

from collections import Counter
from itertools import count
for i in count(2):
    if len(Counter(factorize(i))) == 4 and len(Counter(factorize(i+1))) == 4 and len(Counter(factorize(i+2))) == 4 and len(Counter(factorize(i+3))) == 4:
        print (i)
        break