require 'mathn'
 
def isPrime(n)
  n = n.to_i
  return n.prime?
end

result_cnt=0
result_sum=0
n=9

while (result_cnt < 11)
    all_prime = true
    
    n_str = n.to_s
    n_len = n_str.length
    
    temp=""
    (0..n_len-1).each do |i|
      temp = temp+n_str[i,1]
      
      unless isPrime(temp)
        all_prime = false
        break
      end
    end
    
    temp=""
    n_str.reverse!
    (0..n_len-1).each do |i|
      temp = n_str[i,1] + temp
      
      unless isPrime(temp)
        all_prime = false
        break
      end
    end
    
    if all_prime
      result_cnt+=1
      result_sum+=n
    end
    
    n+=1
end

puts result_sum