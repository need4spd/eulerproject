def isPalidrome(n)
  n_str = n.to_s
  reverse_str = n_str.reverse
  
  return n_str == reverse_str
end

result=0

(0..1000000).each do |n|
  n_2 = n.to_s(2)
  
  unless isPalidrome(n)
    next
  end
  
  if n_2[0,1] == 0
    next
  end
  
  unless isPalidrome(n_2)
    next
  end
  
  result+=n
end

puts "#{result}"
