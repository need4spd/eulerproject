#generate alphabet score
#alphaList=map(chr, range(ord('A'), ord('Z')))
alphaList = [chr(c) for c in range(ord('A'), ord('Z')+1)]

print (alphaList)
def getNameAndIndex(dataList):
            
    for index in range(0, len(dataList)):
        name = dataList[index]
        
        print("name={0}, index={1}".format(name, index+1))
        
        yield name, index+1       

def getNameScore(name):
    sum=0    
    for c in name:
        sum=sum+alphaList.index(c)+1
        print("c={0}, score={1}, namescore={2}".format(c, alphaList.index(c)+1, sum))        
            
    return sum

totalScore=0
indexOfName=0

sampleFile=open("names.txt", "r")
    
names=sampleFile.readlines()
namesStr=names[0]
namesStr=namesStr.rstrip("\n")

#print (namesStr.replace("\"","").split(","))
nameList = namesStr.replace("\"","").split(",")
nameList.sort()

for name, index in getNameAndIndex(nameList):
    (oldTotalScore, totalScore) = (totalScore, totalScore + (getNameScore(name) * (index)))
    
    print ("total score : {0}, minus : {1}".format(totalScore, totalScore-oldTotalScore))

print ("total score : {0}".format(totalScore))
