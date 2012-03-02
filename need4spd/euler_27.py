def isPrime(n):
    # http://www.daniweb.com/software-development/python/code/216880
    '''check if integer n is a prime'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2: 
        return True    
    # all other even numbers are not primes
    if not n & 1: 
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def getResult(a,b,n):
    r = n**2 + (a*n) + b
    
    return r

max_n = 0
max_a = 0
max_b = 0

for a in range(-999, 1000):
    
    for b in range(-999, 1000):
        
        n = 0
        
        while True:
            if isPrime(a+b+1) and isPrime(b):
                r = getResult(a,b,n)
                if isPrime(r):
                    n+=1
                else:
                    break
            else:
                break
        
        if n > max_n:
            print ("a : {0}, b : {1}, n : {2}".format(a,b,n))
            max_n = n
            max_a = a
            max_b = b
        
print (max_a * max_b)