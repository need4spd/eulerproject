#Pandigital 생성
import itertools
 
p=list()
permutations=list(itertools.permutations(list(range(0,10)),10))
for t in permutations:
    s="".join(str(n) for n in t)
    p.append(s)

sum_of_result = 0

rule = {1:2, 2:3, 3:5, 4:7, 5:11, 6:13, 7:17}
for pandigital in p:
    isRight = True
    for k in rule.keys():
        if not int(pandigital[k:k+3]) % rule[k] == 0:
            isRight = False
            break
    
    if isRight:
        sum_of_result += int(pandigital)

print (sum_of_result)
    