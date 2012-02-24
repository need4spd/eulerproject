# xinuguru님의 function
def getDivisors(N):
    divisors = []
    for i in range(1, int(N**0.5)+1):
        if N % i == 0:
            divisors += [i, N/i]
    divisors.remove(N)
    divisors.sort()
    
    if N==110:
        print("divisros : {0}".format(divisors))
        
    return sorted(list(set(divisors)))

def isAbundant(N):

    divisors = getDivisors(N)
    total = sum(divisors)
    
    #if N < total:
        #print(N)
        
    #print("N : {0}, divsors : {1}".format(N, divisors))
    if N < total:
        return True
    else:
        return False
    
    
limit = 28123

abundantList = [n for n in range(12, limit) if isAbundant(n)]

#print (abundantList)

sumOfAbundant = set()
for i in abundantList:
    for j in abundantList:
        if i+j < limit:
            sumOfAbundant.add(i+j)

#a=sum(range(1,limit))
#b=sum(sumOfAbundant)

#print ("a : {0}, b : {1}".format(a,b))

total = sum(range(1,limit)) - sum(sumOfAbundant)

print(total)