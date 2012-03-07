fileUrl = 'list.txt'
arrAll = list()

fo = open(fileUrl, "r")
strAll = ''

while(True):
    ln = fo.read()
    if not ln:
        break
    
    strAll = ln.replace('\n', '')
    
fo.close()

currIdx = 0
multi = 1
while(True):
    currIdx += 1
    currNum = strAll[currIdx-1:currIdx]
    #print(currNum)
    if(currNum != ''):
        multi*=int(currNum)
    if(currIdx%5 == 0):
        #print("ttt")
        arrAll.append(multi)
        multi=1
        
    if(currIdx > len(strAll)): break

print(arrAll)
print(max(arrAll))