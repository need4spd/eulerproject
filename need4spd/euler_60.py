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
    
max = 10000
min = 1
prime_list = [str(n) for n in range(min, max) if isPrime(n)]

def allPrime(iterable):
    for element in iterable:
        if not isPrime(int(element)):
            return False
    return True

print (prime_list)

for p1 in range(0, len(prime_list)-4):  
  for p2 in range(p1+1, len(prime_list)-3):
    if not isPrime(prime_list[p1] + prime_list[p2]) or not isPrime(prime_list[p2] + prime_list[p1]):
      continue
    
    for p3 in range(p2+1, len(prime_list)-2):
      if not isPrime(prime_list[p1] + prime_list[p3]) or not isPrime(prime_list[p3] + prime_list[p1]) or not isPrime(prime_list[p2] + prime_list[p3]) or not isPrime(prime_list[p3] + prime_list[p2]):
        continue
    
      for p4 in range(p3+1, len(prime_list)-1):
        if not isPrime(prime_list[p1] + prime_list[p4]) or not isPrime(prime_list[p4] + prime_list[p1]) or not isPrime(prime_list[p2] + prime_list[p4]) or not isPrime(prime_list[p4] + prime_list[p2]) or not isPrime(prime_list[p3] + prime_list[p4]) or not isPrime(prime_list[p4] + prime_list[p3]):
          continue
          
        for p5 in range(p4+1, len(prime_list)):
          if not isPrime(prime_list[p1] + prime_list[p5]) or not isPrime(prime_list[p5] + prime_list[p1]) or not isPrime(prime_list[p2] + prime_list[p5]) or not isPrime(prime_list[p5] + prime_list[p2]) or not isPrime(prime_list[p3] + prime_list[p5]) or not isPrime(prime_list[p5] + prime_list[p3]) or not isPrime(prime_list[p4] + prime_list[p5]) or not isPrime(prime_list[p5] + prime_list[p4]):
            continue
          
          print (prime_list[p1], prime_list[p2], prime_list[p3], prime_list[p4], prime_list[p5], int(prime_list[p1])+int(prime_list[p2])+int(prime_list[p3])+int(prime_list[p4])+int(prime_list[p5]))
