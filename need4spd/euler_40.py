s=""
for n in range(0, 300000):
   s=s+str(n)
   
   if (len(s) > 1000000):
        break


r = int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])
print(r)
