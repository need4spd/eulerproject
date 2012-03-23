sampleFile=open("euler_42_words.txt", "r")     
names=sampleFile.readlines()
namesStr=names[0]
namesStr=namesStr.rstrip("\n") 
#print (namesStr.replace("\"","").split(","))
nameList = namesStr.replace("\"","").split(",")
 
#Euler 22
alphaList = [chr(c) for c in range(ord('A'), ord('Z')+1)]
def getNameScore(name):
    sum=0  
    for c in name:
        sum=sum+alphaList.index(c)+1
        #print("c={0}, score={1}, namescore={2}".format(c, alphaList.index(c)+1, sum))        
              
    return sum
     
import math
def isTriangeNumber(n):
 
  temp_n = n * 2
   
  start_num = int(math.sqrt(temp_n)) - 1
   
  while True:
    s = start_num**2 + start_num
    if temp_n == s:
      return True
     
    if temp_n < s:
      return False
     
    start_num += 1
 
cnt_of_result = 0
for name in nameList:
  name_score = getNameScore(name)
   
  if isTriangeNumber(name_score):
    cnt_of_result += 1
 
print (cnt_of_result)