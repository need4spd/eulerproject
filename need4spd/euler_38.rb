def isPandigital(n)
  temp_array = Array.new
  
  if n.length == 9
    n.each_char { |c| temp_array.push(c) }
    
    temp_array.sort!
    
    temp_s = temp_array.join
    
    if temp_s.include? "123456789"
      return true
    end
  end
  
  return false
end

result = 0

(9183..9877).each do |n|
  a1 = (n * 1).to_s + (n * 2).to_s
  if isPandigital(a1)
    if result < a1.to_i
      result = a1.to_i
    end
  end
end

puts result
