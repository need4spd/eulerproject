n = 0
(1..1000).each do |i|
  n = n + i**i
end

puts n.to_s[n.to_s.length() - 10, 10]
