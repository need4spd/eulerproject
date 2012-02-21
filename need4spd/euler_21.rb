def getDivisors(num)
    
  divisors=Array.new(0)
  startnum = 1
  
  if num==1
    divisors.push(1)
    return divisors
  end
  
  while True
    
    if num%startnum == 0
        divisors.push(startnum)
    end
    
    startnum+=1
    if num==startnum
        break
    end
  end
  return divisors
end

targetnum=10000
resultList=Array.new(1, 0)

while (true)
  if resultList.count(targetnum) > 0
     targetnum=targetnum-1
     continue      
  end      
        
  divisors=getDivisors(targetnum) #targetnum 220
  sumOfDivisors=sum(divisors) #sumofDivisors 284
        
  tempDivisors=getDivisors(sumOfDivisors)
  tempSumOfDivisors=sum(tempDivisors)
        
  if targetnum==tempSumOfDivisors and targetnum != sumOfDivisors
     resultList.append(targetnum)
     resultList.append(sumOfDivisors)
  end
  
  targetnum=targetnum-1
        
  if targetnum==0
      break
  end
end

puts "result #{resultList}"