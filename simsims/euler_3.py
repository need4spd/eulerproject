def primeFactor(cc):
  for x in range(2, cc+1):
    if cc % x == 0:
      break
  return x

a = 600851475143
result = 0
while a > 1:
  b = primeFactor(a)
  if b > result:
    result = b
  a = int(a/b)
print(result)
  
