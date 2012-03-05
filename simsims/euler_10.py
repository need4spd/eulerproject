import math
def isPrime(a):
  for x in range(2,int(math.sqrt(a))+1):
    if a % x == 0:
        return 0
  return 1

p=3
sum = 2
while True:
  if isPrime(p) == 1:
    sum +=p
  if p >= 2000000:
    break
  p+=2
print(sum)