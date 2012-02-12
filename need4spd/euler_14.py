def a(num):
	return int(num/2)

def b(num):
	return (3*num) + 1

targetnum=1000000
loopCnt=1

biggestLoopCnt=0
biggestLoopCntNum=0

r=targetnum
while True:
	
	if r%2 == 0:
		r=a(r)
		
	else:
		r=b(r)
		
	loopCnt+=1
	
	if r==1:
		if biggestLoopCnt < loopCnt:
			biggestLoopCnt = loopCnt
			biggestLoopCntNum=targetnum
		
		loopCnt=1		
		targetnum-=1
		r=targetnum
	
	if targetnum==1:
		break

print("big", biggestLoopCntNum)