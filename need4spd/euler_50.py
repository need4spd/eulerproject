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

prime_list = [int(n) for n in range(2, 1001) if isPrime(n)]
prime_list.sort()
r = 0
while True:
  r = sum(prime_list)
  
  if r > 1000:
    del prime_list[len(prime_list) - 1]
    continue
    
  if isPrime(r):
    print (r)
    break
  else:
    del prime_list[len(prime_list) - 1]
