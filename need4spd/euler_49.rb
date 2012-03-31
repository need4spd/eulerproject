require 'mathn'
  
def isPrime(n)
  return n.prime?
end

def is_permutations(a,b,c)
  s_a = a.to_s.split(//).sort()
  s_b = b.to_s.split(//).sort()
  s_c = c.to_s.split(//).sort()
  
  if s_a == s_b and s_b == s_c
    return true
  else
    return false
  end
end

prime_list = Array.new
(1000..9999).each do |n|
  if isPrime(n)
    prime_list.push(n.to_i)
  end
end
prime_list.sort!

prime_list.each do |a|
  prime_list.each do |b|
    prime_list.each do |c|
      if b-a == c-b and not b-a == 0
        if is_permutations(a,b,c)
          puts a,b,c
          break
        end
      end
    end
  end
end
