sum=1
rows=1001

(3..1001).step(2) do
  |n|
  up_r = n**2
  up_l = up_r - (n-1)
  dn_l = up_l - (n-1)
  dn_r = dn_l - (n-1)
  
  puts "#{up_r}, #{up_l}, #{dn_l}, #{dn_r}"
  sum = sum + up_r + up_l + dn_l + dn_r
end

puts sum