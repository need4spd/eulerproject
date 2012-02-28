def maxPrimeFactor(n):
    #n = 13195
    divisor = 2
    primeNumbers=list()
    
    while ( divisor <= n ):
        
        if n%divisor == 0:
            primeNumbers.append(divisor)
            n = n/divisor
            divisor=divisor+1
        else:
            divisor=divisor+1
            
    return primeNumbers[len(primeNumbers) - 1]