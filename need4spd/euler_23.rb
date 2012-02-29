require 'set'

def getDivisors(num)
  divisors=Set.new
  l=Math.sqrt(num).to_i
  
  for i in (1..l+1)
    if num % i == 0
      divisors.add(i)
      divisors.add(num/i)
    end
  end
  
  divisors.delete(num)
  divisors = divisors.to_a
  divisors.sort!
  
  if num==110
    puts "divisors : #{divisors}"
  end
  return divisors
end

def isAbundant(num)
  divisors = getDivisors(num)
  total = divisors.inject(:+)
  
  #puts "num  : #{num}, total : #{total}"
  if num < total
    #puts num
  end
  
  if num < total
    return true
  else
    return false
  end
end
    
    
limit = 28123

abundantList = (12..limit).to_a.select{|v| isAbundant(v)}

#puts "list : #{abundantList}"
sumOfAbundant = Set.new
for i in abundantList
    for j in abundantList
        if i+j < limit
            sumOfAbundant.add(i+j)
        end
    end
end

#a=(1..limit-1).to_a.inject(:+)
#b=sumOfAbundant.inject(:+)

#puts "a : #{a}, b : #{b}"
total = (1..limit-1).to_a.inject(:+) - sumOfAbundant.inject(:+)

puts total
