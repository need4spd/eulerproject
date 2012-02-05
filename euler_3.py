def primefactors(num):
  startnum=2
  primeNumbers=list()
  
  quota=0
  rest=0
  
  while True:
    quota=num/startnum
    rest=num%startnum
    
    #print("quota="+quota+", rest="+rest+", startnum="+startnum)
      
    if rest==0:
      primeNumbers.append(startnum)
      startnum=2
      num=quota
    else:
      startnum=startnum+1
      
    if quota==1 and rest==0:
      break
  
  return primeNumbers

primeNumbers=primefactors(600851475143)
print (primeNumbers)

primeNumbers.sort(reverse=True)
print (primeNumbers[0])

