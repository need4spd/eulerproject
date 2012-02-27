def fib(n)
  curr = 0
  succ = 1

  n.times do |i|
    curr, succ = succ, curr + succ
  end

  return curr
end


n = 1
while true
  r = fib(n)
  
  puts "#{r.to_s.length}"
  
  if r.to_s.length == 1000
    puts "#{n}"
    
    break
    
  end
  
  n+=1
  
end
