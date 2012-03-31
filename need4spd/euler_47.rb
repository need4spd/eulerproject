require 'set'

def primefactors(num)
  startnum=2
  primeNumbers=Set.new
   
  quota=0
  rest=0
   
  while true
    quota=num/startnum
    rest=num%startnum
    #puts "quota=#{quota}, rest=#{rest}, startnum=#{startnum}"
       
    if rest==0
      primeNumbers.add(startnum)
      startnum=2
      num=quota
    else
      startnum=startnum+1
    end
       
    if quota==1 and rest==0
      break
    end
     
  end
   
  return primeNumbers
end

n = 2
cnt_of_continue = 0
while (true)
  prime_factors = primefactors(n)
  
  if prime_factors.length() == 4
    cnt_of_continue += 1
  else
    cnt_of_continue = 0
  end
  
  if cnt_of_continue == 4
    puts n-3
    break
  end
  
  n += 1
end