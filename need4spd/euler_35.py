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

def getCircularList(n):
    n_list = [c for c in (str(n))]
    
    result_list = list()
    loop_cnt = len(str(n)) - 1
        
    result_list.append(n)
    
    while (loop_cnt > 0):
        t = n_list.pop(-1)
        n_list.insert(0, t)
        
        result_list.append(int("".join(str(c) for c in n_list)))
        loop_cnt = loop_cnt - 1
    
    return result_list
        
r_list = list()

for n in range(0,1000000):
    n_str = str(n)
    
    if n_str != 2 and "2" in n_str:
        next
    
    if "0" in n_str:
        next
    
    c_list = getCircularList(n)
    all_prime=True
    
    for p in c_list:
        if not isPrime(p):
            all_prime = False
            break
    
    if all_prime:
        r_list.append(n)
        
print (len(r_list))
print (r_list)