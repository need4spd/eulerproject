r=0
for a in range(100, 999):
  for b in range(100,999):
    c = a*b
    if c > 99999:
      if int(c / 100000) == c%10 and int(c/10000)%10 == int((c%100)/10) and int(c/1000)%10 == int((c%1000)/100) :
        if r < c:
          r = c
print(r)