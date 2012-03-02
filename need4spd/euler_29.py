r=set()

for a in range(2,101):
    for b in range(2,101):
        r.add(a**b)

print(r, len(r))