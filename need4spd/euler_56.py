max_l = list()

for a in range(1, 101):
  for b in range(1, 101):
    n = a ** b
    n_list = list(str(n))
    
    s = 0
    for c in n_list:
      s = s + int(c)
    max_l.append(s)
    
print (max(max_l))
