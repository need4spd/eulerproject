
cnt=0
for x in range(1, 10):
    for n in range(1, 100):
        if n == len(str(x**n)):
            cnt+=1
print (cnt)