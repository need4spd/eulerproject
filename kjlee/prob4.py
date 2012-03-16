#prob4: symmetry number

def check(num):
	a = 0
	temp = num
	
	while temp > 0:
		temp /=10
		a += 1
	
	n = 0
	list1 = []
	list2 = []
	   	
	for i in range(a):
		n = num % 10
		num = num / 10
		list1.append(n)
		
	list2 = list1[:]
	list1.reverse()
		    
	if list2 == list1:
		return True


result = []
for i in range(101,1000):
	for j in range(101,1000):
		if check(i*j) == True:
			result.append(i*j)
			  
print(max(result))

