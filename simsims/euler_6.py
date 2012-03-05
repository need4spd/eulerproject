import math
a = 0
b = 0
for x in range(1,101):
  a += math.pow(x,2)
  b += x
print(math.pow(b,2)-a)