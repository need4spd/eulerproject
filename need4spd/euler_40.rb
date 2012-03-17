s=""
(0..300000).each do |n|
  s=s+n.to_s()
  
  if (s.size > 1000000)
    break
  end
end

puts s

r=s[1].to_i * s[10].to_i * s[100].to_i * s[1000].to_i * s[10000].to_i * s[100000].to_i * s[1000000].to_i
puts r
