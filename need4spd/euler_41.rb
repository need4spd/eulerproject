require 'mathn'
 
def isPrime(n)
  return n.prime?
end

p=Array.new

p = p + "123".split("").permutation.to_a
p = p + "1234".split("").permutation.to_a
p = p + "12345".split("").permutation.to_a
p = p + "123456".split("").permutation.to_a
p = p + "1234567".split("").permutation.to_a
p = p + "12345678".split("").permutation.to_a
p = p + "123456789".split("").permutation.to_a

p.sort!

result = 0

p.each do |n|
  s=n.join("")
  
  if (isPrime(s.to_i))
    if result < s.to_i
      result = s.to_i
    end
  end
end

puts result