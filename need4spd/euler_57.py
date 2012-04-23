n = 3
d = 2
r = 0
 
for x in range(2, 1001):
    n, d = n + d * 2, n + d
    if len(str(n)) > len(str(d)): 
      r += 1
 
print (r)