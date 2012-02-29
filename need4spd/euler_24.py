import itertools

l=list(range(0,10))
permutations=list(itertools.permutations(l,10))

p=list()
for t in permutations:
    s="".join(str(n) for n in t)
    p.append(s)
    #print(s)

p.sort()

print(p[999999])
