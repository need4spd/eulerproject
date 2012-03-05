def primeList(a):
  pList = []
  while a > 1 :
    for x in range(2,a+1):
      if a % x == 0:
        a = int(a/x)
        pList.append(x)
        break
  return pList

a=2
for x in range(3,21):
  c = primeList(x)
  t = a
  for y in c:
    if t % y != 0:
      a = a*y
    else :
      t = int(t/y)
print(a)