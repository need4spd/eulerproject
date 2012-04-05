import math

def get_number_of_cases(n, r):
  r = (math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
  return r

cnt = 0
for n in range(23, 101):
  for r in range(1, n-1):
    if get_number_of_cases(n, r) > 1000000:
           cnt += 1
print (cnt)