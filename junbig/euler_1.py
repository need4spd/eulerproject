a=0;
b=0;
for i in range(1,1000,1):
  if i % 3 == 0:
      a += i
  elif i%5 == 0:
      b += i

print(a+b)
