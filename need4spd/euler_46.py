
def isPrime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True 
    if not n & 1: 
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def getPrimeNumberList(offset):
    result_list = list()
    numberOfPrimeNum = 0
    
    targetNum=2
     
    while True:
        r=isPrime(targetNum)
         
        if r:
            result_list.append(targetNum)
            numberOfPrimeNum=numberOfPrimeNum+1
             
            if numberOfPrimeNum == offset:
                return result_list
         
        targetNum=targetNum+1
         
    return result_list
    
x = 5

import math

while True:
  prime_list = getPrimeNumberList(x)
    
  if x in prime_list:
    x += 2
    continue
  
  #print (x)
  temp_list = list()
  for n in range(1, int(math.sqrt(x))):
    for p in prime_list:
      temp_x = p + 2 * (n**2)
      
      if temp_x > x:
        break
        
      if temp_x == x:
        temp_list.append(True)
        
        #print (n, x, p)
        
      else:
        temp_list.append(False)
  
  #print (temp_list)
  
  if not any(temp_list):
    print (x)
    break
  
  x += 2
  