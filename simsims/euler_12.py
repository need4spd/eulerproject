def divisorCnt(a):
  pdict = dict()
  while a > 1:
    for x in range(2,a+1):
      if a%x == 0:
        a = int(a/x)
        try:
          pdict[x] = pdict[x]+1
        except:
          pdict[x] = 1
        break
  cnt =1
  for y in pdict.values():
    cnt = cnt * (y+1)
  return cnt

cur = 3
idx = 3
while True:
  if divisorCnt(cur) >= 500:
    break
  cur += idx
  idx +=1
print(cur)