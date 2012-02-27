def prime(num) :
	j=2
	isPrime = False
	while(j <= num) :
		if(j!=num and num%j==0) :
			isPrime = False
			break
		else :
			isPrime = True
		j=j+1
	return isPrime	
	
list=[]
a=600851475143
b=1
max=0
while(b <= a) :
	if(a%b == 0 and prime(b) == True) :
		a = a/b
		list.append(b)
		if(max < b) : max=b
	b=b+1	

print(max)