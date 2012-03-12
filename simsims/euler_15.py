gSize = 12
pEdge = dict()
pVertex = list()
pPath = list()

def dfs(a, b):
  cnt = 0
  if a == b:
    return 1
  if a%gSize != gSize-1 and pEdge[(a,a+1)]:
    pVertex[a+1] = False
    pPath.append(a+1)
    cnt += dfs(a+1,b)
    pVertex[a+1] = True
    pPath.remove(a+1)
    
  if a+gSize < gSize*gSize and pEdge[(a,a+gSize)]:
    pVertex[a+gSize] = False
    pPath.append(a+gSize)
    cnt += dfs(a+gSize,b)
    pVertex[a+gSize] = True
    pPath.remove(a+gSize)
  if a < gSize:
    print(cnt)
  return cnt

for x in range (0,gSize*gSize):
    if x%gSize != gSize-1:
      pEdge[(x,x+1)] = True
    if x+gSize < gSize*gSize:
      pEdge[(x,x+gSize)] = True
    pVertex.append(True)
pPath.append(0)
cc=dfs(0,gSize*gSize-1)
print(cc)  
