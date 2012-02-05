def sumofsquare(numberList):
	result=sum([x**2 for x in numberList])
	return result

def squareofsum(numberList):
	import math
	result=math.pow(sum(numberList), 2)
	return result
	
#print(sumofsquare(range(1,11))
#print(squareofsum(range(1,11))

r = sumofsquare(range(1,101))
print(r)

r2 = int(squareofsum(range(1,101)))
print(r)

print(r2-r)