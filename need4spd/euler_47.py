def primefactors_limit_count(num):

  num_of_factors = 0
  limit_cnt = 3
  
  startnum=2
  primeNumbers=set()
   
  quota=0
  rest=0
   
  while True:
    quota=num/startnum
    rest=num%startnum
     
    if rest==0:
      num_of_factors += 1
      primeNumbers.add(startnum)
      startnum=2
      num=quota
    else:
      startnum=startnum+1
       
    if quota==1 and rest==0:
      break
    
    if num_of_factors > limit_cnt:
      break
      
  return primeNumbers

n = 2
cnt_of_continue = 0
while True:
  prime_factors = primefactors_limit_count(n)
  
  if len(prime_factors) == 3:
    cnt_of_continue += 1
  else:
    cnt_of_continue = 0
  
  if cnt_of_continue == 3:
    print(n - 2)
    break
  n += 1
    