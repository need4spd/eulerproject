def getDivisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors += [int(i), int(n/i)]
    #divisors.remove(n)
    divisors.sort()
    
    #print("divisros : {0}".format(divisors))
         
    return sorted(list(set(divisors)))
    
r=0
for n in range(2, 100000):
    
    if '0' in str(n):
        continue
    
    l = getDivisors(n)

    end_offset=len(l)-1
    start_offset=0
    
    while (start_offset!=end_offset and start_offset <= end_offset):
        a=l[start_offset]
        b=l[end_offset]
        
        start_offset+=1
        end_offset-=1
                
        if '0' in str(a) or '0' in str(b):
            continue
        
        joined_n = str(a)+str(b)+str(n)
        if (len(joined_n) == 9):
            temp_l = ''.join(sorted([ c for c in joined_n]))
            
            if '123456789' in temp_l:
                print(a,b,n)
                r+=n
                break
                
        

print ("result : {0}".format(r))