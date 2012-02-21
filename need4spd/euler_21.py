def getDivisors(num):
    
  divisors=list()
  startnum = 1
  
  if num==1:
    divisors.append(1)
    return divisors

  while True:
    
    if num%startnum == 0:
        divisors.append(startnum)
    
    startnum+=1
    if num==startnum:
        break
    
  return divisors    

if __name__ == '__main__':
    targetnum=10000
    resultList=list()
    while True:
        
        print("############################################ targetnum : {0}".format(targetnum))
        
        if resultList.count(targetnum) > 0:
            print("continue!! {0}".format(targetnum))
            targetnum=targetnum-1
            continue
        
        divisors=getDivisors(targetnum) #targetnum 220
        sumOfDivisors=sum(divisors) #sumofDivisors 284
        
        tempDivisors=getDivisors(sumOfDivisors)
        tempSumOfDivisors=sum(tempDivisors)
        
        if targetnum==tempSumOfDivisors and targetnum != sumOfDivisors:
            resultList.append(targetnum)
            resultList.append(sumOfDivisors)
            
            print("resultList!! {0}, {1}".format(targetnum, sumOfDivisors))
            print("resultList!! {0}".format(resultList))
    
        targetnum=targetnum-1
        
        if targetnum==0:
            break
        
    
    print (resultList)
    print (sum(resultList))