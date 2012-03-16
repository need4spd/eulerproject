rList = dict()
def collatzCnt(a):
  cnt = 1
  t=a
  while t != 1:
    if rList.get(t) != None:
      rList[a] = cnt + rList.get(t) - 1
      return (a,rList[a])
    if t % 2 ==0:
      t = int(t/2)
    else:
      t = 3*t +1
    cnt += 1
  rList[a] = cnt
  return (a,cnt)

r= (0,0)
for x in range(1, 1000001):
  t = collatzCnt(x)
  if t[1] > r[1]:
    r = t
print(r[0])