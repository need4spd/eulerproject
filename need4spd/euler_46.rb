require 'mathn'
  
def isPrime(n)
  return n.prime?
end

def getPrimeNumber(offset)
    numOfPrime=0
    targetNum=2
    result_list = Array.new
     
    while true
        r=isPrime(targetNum)
        if r
            numOfPrime+=1
            result_list.push(targetNum)
             
            if numOfPrime == offset
                return result_list
            end
        end
         
        targetNum+=1
     
    end
     
    return result_list
end

x = 5

while(true)
  prime_list = getPrimeNumber(x)
  
  if prime_list.include?(x)
    x += 2
    next
  end
  
  temp_list = Array.new
  (1..Math.sqrt(x).to_i).each do |n|
    prime_list.each do |p|
      temp_x = p + 2 * (n**2)
      
      if temp_x > x
        break
      end
      
      if temp_x == x
        temp_list.push(true)
      else
        temp_list.push(false)
      end
    end
  end
  
  if not temp_list.any? {|b| b == true}
    puts x
    break
  end
  x += 2
end