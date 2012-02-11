numlist=list()
sampleFile=open("euler_13_problem.txt", "r")
for l in sampleFile.readlines():
	l=l.rstrip('\n')
	numlist.append(int(l))

sumofnumbers=sum(numlist)

print(str(sumofnumbers)[0:10])