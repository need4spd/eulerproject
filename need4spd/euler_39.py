r=dict()

for a in range(1,1000):
    for b in range(1,1000):
        for c in range(1,1000):
            
            #print(a,b,c)
            
            if (a+b+c > 1000):
                break
            temp = a**2 + b**2
            
            if (c**2 == temp):
                p=a+b+c
                
                if(p in r):
                    r[p]=r[p]+1
                else:
                    r[p]=1

max_key = sorted(r, key=r.get, reverse=True)[0]

print(max_key)
