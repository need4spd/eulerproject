matrix=[]

sampleFile=open("euler_11_prb.txt" ,"r")
for l in sampleFile.readlines():
	l=l.rstrip('\n')
	matrix.append(l.split(" "))
	
print(matrix)

biggestNum=0

#first rule

for rowindex in range(0,1):
	selectedRow=matrix[rowindex]
		
	print(selectedRow)
	for columnindex in range(4,20):
		print(columnindex)
		slicedList=selectedRow[columnindex:columnindex-4:-1]
		
		print(slicedList)
		
		