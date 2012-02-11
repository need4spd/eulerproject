def numberOfPrimeFactors(num):

	if num==1:
		return 1
	
	startnum=2	
	exponentDict=dict()
	
	quota=0
	rest=0
	
	while True:
		quota=num/startnum
		rest=num%startnum
		
		if rest==0:
			if startnum in exponentDict:
				exponentDict[startnum] = exponentDict.get(startnum) + 1
			else:
				exponentDict[startnum]=1
				
			startnum=2
			num=quota
		else:
			startnum+=1
		
		if quota==1 and rest==0:
			break
	# 소인수분해 끝. 약수의 개수를 구한다.
	l=exponentDict.values()
	
	r=1
	for x in l:
		r = r * (x+1)
		
	return r

#삼각수구하기

import time

tic = -time.clock()
i=1
result=0
while True:
	result+=i
	i+=1
	
	#소인수분해를하여 약수의 개수를 받아낸다
	numberOfPrime=numberOfPrimeFactors(result)
	
	if numberOfPrime >= 500:
		print(result)
		break
tic+=time.clock()

print("in"+str(tic)+"s")