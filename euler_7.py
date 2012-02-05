def isPrimeNumber(num):
	t=2
	
	while t<=num:
		rest=num%t
		
		if rest==0 and t==num:
			return True
		elif rest==0 and t!=num:
			return False
		else:
			t=t+1

	return False

def getPrimeNumber(offset):
	numberOfPrimeNum=0
	
	targetNum=2
	
	while True:
	
		r=isPrimeNumber(targetNum)
		
		if r:
			numberOfPrimeNum=numberOfPrimeNum+1
			
			if numberOfPrimeNum == offset:
				return targetNum
		
		targetNum=targetNum+1
		
	return targetNum

r=getPrimeNumber(10001)
print(r)