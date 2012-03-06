require 'mathn'
 
def isPrime(n)
  return n.prime?
end

def getCircularList(n)
  n_list = Array.new
  n.to_s.each_char{|c| n_list.push(c)}
  
  result_list = Array.new
  loop_cnt = n.to_s.length - 1
  
  result_list.push(n)
  
  while (loop_cnt > 0)
    n_list.rotate!
    result_list.push(n_list.join.to_i)
    loop_cnt -= 1
  end
  
  return result_list
end

r_list = Array.new

(0..999999).each do |n|
  n_str = n.to_s
  
  if n_str != 2 and n_str.include? "2"
    next
  end
  
  if n_str.include? "0"
    next
  end
  
  c_list = getCircularList(n)
  all_prime = true
  
  c_list.each do |c|
    if not isPrime(c)
      all_prime = false
      break
    end
  end
  
  if all_prime
    r_list.push(n)
  end
end

puts r_list.size