def getPrimes(maxCnt):
    primes = list()
    totCnt = 0
    startNum = 2
    primes.append(startNum)
    
    loopCnt = 2
    while(True):
        startNum += 1
        isPrime = True
        for x in primes:
            if(startNum % x == 0):
                isPrime = False
                break
        
        if(isPrime): 
            loopCnt+=1
            primes.append(startNum)
        
        if(loopCnt > maxCnt): break
    
    return primes

arrPrimes = getPrimes(100)
print(arrPrimes)
print(max(arrPrimes))
        
        