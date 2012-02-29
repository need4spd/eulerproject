a=1
b=2
list=[a,b]
while a+b <= 4000000 :
	list.append(a+b)
	a,b= b,a+b

	
sum=0
for c in list:
	if c%2==0: sum=sum+c

print(sum)