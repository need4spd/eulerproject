import math

limit = 999999
result = 0

for n in range(3, limit+1):
    n_str = str(n)
    
    temp = 0
    for i in n_str:
        temp = temp + math.factorial(int(i))
    
    if temp == n:
        result += n

print (result)