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
   
  #divisors.delete(num)
  divisors = divisors.to_a
  divisors.sort!

  return divisors
end
r=0
(2..100000).each do |n|
  if n.to_s.include? "0"
        next
  end
  
  l = getDivisors(n)
  
  end_offset=l.length-1
  start_offset=0
  
  while (start_offset != end_offset and start_offset <= end_offset)
    a=l[start_offset]
    b=l[end_offset]
    
    start_offset+=1
    end_offset-=1
    
    if a.to_s.include? "0" or b.to_s.include? "0"
      next
    end
    
    joined_n = a.to_s + b.to_s + n.to_s
    
    temp_l = Array.new
    
    if(joined_n.length == 9)
      joined_n.each_char{|c| temp_l.push(c)}
      temp_l.sort!
      temp_s = temp_l.join
      if temp_s.include? "123456789"
        puts "#{a}, #{b}, #{n}"
        r+=n
        break
      end
    end
  end
end

puts r