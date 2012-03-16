xList = list()
xSize = 21
for x in range(1, xSize+1):
  cDict = dict()
  cDict[0] = 0
  cSum =0
  for y in range(1,x):
    cDict[y] = cDict[y-1] + xList[x-2].get(y)
    cSum += cDict[y]
  if x > 1:
    cDict[x] = cSum
  else:
    cDict[x] = 1
  xList.append(cDict)

print(sum(xList[xSize-1].values()))