def get_answer():
    cubic_map=dict()  
    for n in range(0,100000):
        k="".join(sorted(str(n**3)))
        if not k in cubic_map:
            cubic_map[k]=list()
            cubic_map[k].append(n**3)
        else:
            cubic_map[k].append(n**3)
    
    for k in cubic_map.keys():
        if len(cubic_map[k]) == 5:
            print (cubic_map[k])
            break

if __name__ == "__main__":
    get_answer()
else:
    import itertools
    permutations = list(itertools.permutations(list("41063625"), len("41063625")))
    
    p=set()
    for t in permutations:
        s="".join(n for n in t)
        p.add(int(s))
    for k in p:
        if k == 41063625:
            print(k)