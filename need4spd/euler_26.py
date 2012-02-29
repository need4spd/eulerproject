def findRepeatNumLen(n):
    r = 1 / n
    r = str(r)[2:] #0. 제거
    
    repeat_cnt = 1
    
    if len(r) == 1:
        return 1
    
    for i in range(len(r)):
        
        repeat_cnt = 1
        
        for j in range(len(r)-1):
            t1 = r[i]
            t2 = r[j+1]
            
            if t1 == t2:
                return repeat_cnt
            else:
                repeat_cnt+=1

r=0
maxlen=0

for n in range(1, 1001):
    length = findRepeatNumLen(n)
    if maxlen < length:
        maxlen = length
        r = n
    
print (r)