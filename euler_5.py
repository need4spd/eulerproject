numList=range(1,21)

num=1

while True:
  isSearch=True
  for n in numList:
    r=num%n

    if r!=0:
      isSearch=False
      num+=1
      break

  if isSearch:
    print(num)
    break

