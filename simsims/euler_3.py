def primeFactor(idx, data):
  for x in range(idx, data+1):
    if data % x == 0:
      break
  return x

a = 600851475143
b = 2
result = 0
while a > 1:
  b = primeFactor(b, a)
  if b > result:
    result = b
  a = int(a/b)
print(result)
