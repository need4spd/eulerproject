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
 
total=1
rows=1
sumPrime=0

n=3
while True:
    up_r = n**2
    up_l = up_r - (n-1)
    dn_l = up_l - (n-1)
    dn_r = dn_l - (n-1)
     
    total += 4
    rows+=2
    if isPrime(up_r):
      sumPrime+=1
    if isPrime(up_l):
      sumPrime+=1
    if isPrime(dn_l):
      sumPrime+=1
    if isPrime(dn_r):
      sumPrime+=1
    
    #print(total, sumPrime)
    if (sumPrime / total)*100 < 10:
      print(rows)
      break
    
    n+=2
