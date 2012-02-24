a,b,sum = 1,2,0
while b < 4000000:
	if b % 2 == 0:
		sum += b
	a,b = b,a+b
print(sum)
