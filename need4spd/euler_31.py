"""
i=0
a=[0]*6
a[1]=1

for n in range(2, 5):
    a[n]=a[n-1]+n

print (a[4])
"""
n=0
for p1 in range(0, 201):
    for p2 in range(0, 101):
        if(p1 + 2*p2) % 5 != 0:
            continue
        for p5 in range(0, 41):
            for p10 in range(0, 21):
                for p20 in range(0, 11):
                    if(p1+2*p2+5*p5+10*p10+20*p20) %50 != 0:
                        continue
                    for p50 in range(0, 5):
                        for p100 in range(0, 3):
                            for p200 in range(0, 2):
                                s=(p1 + 2*p2 + 5*p5 + 10*p10 + 20*p20 + 50*p50 + 100*p100 + 200*p200)
                                if s == 200:
                                    n+=1
print (n)