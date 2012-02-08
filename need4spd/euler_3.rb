def primefactors(num)
  startnum=2
  primeNumbers=Array.new
  
  quota=0
  rest=0
  
  while true
    quota=num/startnum
    rest=num%startnum
    puts "quota=#{quota}, rest=#{rest}, startnum=#{startnum}"
      
    if rest==0
      primeNumbers.push(startnum)
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

primeNumbers=primefactors(600851475143)
puts primeNumbers

sortedList=primeNumbers.sort {|x,y| y<=>x}
puts sortedList[0]

