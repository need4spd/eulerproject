def myReverse(targetList):
  for index in range(len(targetList) -1, -1, -1):
    yield targetList[index]
    
def isSymmetryNum(targetNumber):
  targetList=list(str(targetNumber))
  result=list()
  
  for char in myReverse(targetList):
    result.append(char)
  
  reversedNum=int(''.join(result))
  
  return targetNumber==reversedNum
    
result=isSymmetryNum(1234)
print (result)

target1=range(1,1000)
target2=range(1,1000)
biggestNum=0

for n1 in target1:
  for n2 in target2:
    a=n1*n2
    
    if isSymmetryNum(a) and biggestNum < a :
      biggestNum=a
      
      
print(biggestNum)


