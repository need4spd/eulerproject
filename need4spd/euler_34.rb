limit = 999999
result = 0

(3..limit).each do
  |n|
  n_str = n.to_s
  
  temp = 0
  n_str.each_char do
    |c|
    
    if c.to_i == 0
      temp = temp + 1
    else
      temp = temp + c.to_i.downto(1).inject(:*)
    end
    
  end
      
  if temp == n
    result += n
  end
end

puts result
