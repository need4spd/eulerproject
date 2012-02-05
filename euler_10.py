def isPrime(n):
	if n==2:
		return True
	elif n%2==0:
		return False
	
	i=3
	
	import math
	range=int(math.sqrt(n))+1
	while i<range:
		if(n%i==0):
			return False
		i+=1
	return True
	
num=2
sumOfPrime=0
while True:
	if isPrime(num):
		sumOfPrime+=num
		
	num+=1
		
	if num==2000000:
		break

print (sumOfPrime)