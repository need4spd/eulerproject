import math
def isPrime(a):
  for x in range(2,int(math.sqrt(a))+1):
    if a % x == 0:
        return 0
  return 1

cnt = 1
p=3
while True:
  if isPrime(p) == 1:
    cnt +=1
  if cnt == 10001:
    break
  p+=2
print(p)