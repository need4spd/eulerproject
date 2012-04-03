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

max = 1000000
prime_list = [int(n) for n in range(2, max+1) if isPrime(n)]
prime_list2 = [int(n) for n in range(2, max+1) if isPrime(n)]

terms = 0
r1 = 0
r2 = 0

result = 0

while True:

  if (len(prime_list) == 0):
    break
    
  r1 = sum(prime_list)
  
  #print (r1, len(prime_list), terms)
  if r1 > max:
    del prime_list[len(prime_list) - 1]
    continue
    
  if isPrime(r1):
    if (terms < len(prime_list)):
      terms = len(prime_list)
      result = r1
  
  del prime_list[len(prime_list) - 1]

    

print (terms, result)
