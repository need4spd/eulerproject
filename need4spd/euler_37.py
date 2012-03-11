def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True   
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

result_cnt=0
result_sum=0
n=9
while (result_cnt < 11):
    all_prime = True
    
    n_str = str(n)
    n_len = len(n_str)
       
    for i in range(0, n_len):
        temp = n_str[0:i+1:1]
        
        if not isPrime(temp):
            all_prime = False
            break
    
    n_str = n_str[::-1]
    
    temp = ""
    for i in range(0, n_len):
        temp = n_str[i:i+1:1] + temp
        
        if not isPrime(temp):
            all_prime = False
            break
        
    if all_prime:
        result_cnt+=1
        result_sum+=n

    n+=1
    
print (result_sum)
print (result_cnt)