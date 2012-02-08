def fib_up_to(max):
	i1=1
	i2=1
	fibList=list()
	
	while i1<=max:
		fibList.append(i1)
		i1,i2=i2,i1+i2
		
	return fibList

result=fib_up_to(4000000)

sum=0
for num in result:
	if num%2==0:
		sum=sum+num

print(sum)

