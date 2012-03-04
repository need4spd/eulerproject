#10n + i / 10i + d = n/d
#9nd = 10in - di
#i = remove num, d=bunmo, n=bunja
# 0 < i < 10

multi_of_d=1
multi_of_n=1

for i in range(1,10):
    for n in range(1, 10):
        for d in range(n+1, 10):
            
            if 9*n*d == ((10*i*n) - (i*d)):
                print("n : {0}, d : {1}, i : {2}".format(n, d, i))
                t=10*i + d
                t2=10*n+i
                
                multi_of_d = multi_of_d * t
                multi_of_n = multi_of_n * t2

print (multi_of_d, multi_of_n, multi_of_d / multi_of_n)
        