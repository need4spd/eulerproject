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

def is_permutatins(a,b,c):
  s_a = list(str(a))
  s_a.sort()
  s_b = list(str(b))
  s_b.sort()
  s_c = list(str(c))
  s_c.sort()
  if s_a == s_b == s_c:
    return True
  else:
    return False
  
prime_list = [int(n) for n in range(1000, 10000) if isPrime(n)]
prime_list.sort()

for a in prime_list:
  for b in prime_list:
    for c in prime_list:
      if b-a == c-b and not b-a == 0:
        if is_permutatins(a,b,c):
          print (a,b,c)
          break
