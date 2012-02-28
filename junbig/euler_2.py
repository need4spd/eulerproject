a = 1
b = 2
c = 0
sum = 0
while c <= 4000000 :
  c = a + b
  if c <= 4000000 and a % 2 == 0 :
    sum += a
  elif c > 4000000 :
    if b % 2 == 0 :
      sum += b
    break 
    
  a = b
  b = c
    
print(sum)

