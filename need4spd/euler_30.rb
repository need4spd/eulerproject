limit=(9**5)*6

r_list=Array.new

(2..limit).each do
  |n|
  n_str = n.to_s
  
  sum=0
  n_str.each_char do
    |c| sum = sum + (c.to_i ** 5)
  end
  
  if (sum==n)
    r_list.push(n)
  end
end

puts r_list.inject(:+)
