n=1
m=2

import math

while True:
	r=math.pow(m,2) + m*n
	
	if r==500:
		print(m, n)
		break
		
	m+=1
	if m==500:
		n+=1
		m=n+1

a=math.pow(m,2) - math.pow(n,2)
b=2*m*n
c=math.pow(m,2) + math.pow(n,2)

print(a, b, c)
print(a+b+c)
print(a*b*c)