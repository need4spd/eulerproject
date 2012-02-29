def check_cycle(d)
  dividend = 1
  n = 0
  remain_list = Array.new
  
  while true
    remain = dividend % d
    
    if remain_list.include?(remain)
      return n - remain_list.index(remain)
    else
      remain_list.push(remain)
      dividend = remain * 10
      n+=1
    end
  end
end

max_d = 0
d = 2
max_n = 0

while d < 1000
  temp = check_cycle(d)
  if temp > max_n
    max_n = temp
    max_d = d
  end
  
  d+=1
  
end

puts max_d