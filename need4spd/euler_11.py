def multiplyOfElements(targetList):
	result=1

	for x in targetList:
		result=result*int(x)
	
	return result
		
matrix=[]

sampleFile=open("euler_11_prb.txt" ,"r")
for l in sampleFile.readlines():
	l=l.rstrip('\n')
	matrix.append(l.split(" "))
	
print(matrix)

biggestNum=0
biggestSlicedList=[]

#first rule
for rowindex in range(0,20):
	selectedRow=matrix[rowindex]
		
	for columnindex in range(4,21):
		slicedList=selectedRow[columnindex-4:columnindex]
	
		r= multiplyOfElements(slicedList)
	
		if biggestNum < r:
			biggestNum=r
			biggestSlicedList=slicedList
	

print ("biggestNum : " + str(biggestNum))
print ("slicedList : " + str(slicedList))

#second rule
for columnindex in range(0,20):
	pivotList=[]

	for rowindex in range(0,20):
		pivotList.append(matrix[rowindex][columnindex])
		
		print("pivotList : " + str(pivotList))
		
	for columnindex in range(4,21):
		slicedList= pivotList[columnindex-4:columnindex]
	
		r= multiplyOfElements(slicedList)
	
		if biggestNum < r:
			biggestNum=r
			biggestSlicedList=slicedList
						
print ("biggestNum : " + str(biggestNum))
print ("slicedList : " + str(slicedList))		

#third rule
for rowLoop in range(0, 17):
	for columnLoop in range(0, 17):
		slicedList=[]
		for arraySize in range(0, 4):
			slicedList.append(matrix[arraySize + rowLoop][columnLoop + arraySize])

		r = multiplyOfElements(slicedList)
		
		if biggestNum < r:
			biggestNum=r
			biggestSlicedList=slicedList
						
print ("biggestNum : " + str(biggestNum))
print ("biggestSlicedList : " + str(biggestSlicedList))

#fourth rule
for rowLoop in range(0, 17):
	for columnLoop in range(3, 19):
		slicedList=[]
		for arraySize in range(0, 4):
			slicedList.append(matrix[arraySize + rowLoop][columnLoop - arraySize])
			
		r = multiplyOfElements(slicedList)
		
		if biggestNum < r:
			biggestNum=r
			biggestSlicedList=slicedList
						
print ("biggestNum : " + str(biggestNum))
print ("biggestSlicedList : " + str(biggestSlicedList))


		
