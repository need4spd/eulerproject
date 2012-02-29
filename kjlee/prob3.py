#prob3.py
import math

num =600851475143
n=int(round(math.sqrt(num)))
  
d = dict()
   
for i in range(2,n):
	cnt = 0
	while num%i == 0:
		num = num/i
		cnt = cnt+1
	if cnt > 0:
		d[i] = cnt
print(d)
   
max = 0
for k in d.keys():
	if max < k:
		max = k
print(max)
	
