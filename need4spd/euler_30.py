
r_list=list()

exponent=5

limit=(9**5)*6

for n in range(2, limit+1):
    n_str = str(n)
    
    if n == sum(int(i) ** 5 for i in n_str):
        r_list.append(n)
        
print(sum(r_list))