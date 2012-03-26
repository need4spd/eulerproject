def is_pentagonal(n)
  n = n.abs
  p = (Math.sqrt(1 + 24*n) + 1) / 6
  
  return p == p.to_i
end

pent_list = [1]

i = 0
not_found = true
while (not_found)
  i+=1
  
  pent_list.push((i * (3*i - 1)/2).to_i)
  
  (2..pent_list.length - 1).each do |j|
    if is_pentagonal(pent_list[i] - pent_list[j]) and is_pentagonal(pent_list[i] + pent_list[j])
      puts pent_list[i] - pent_list[j]
      not_found = false
      break
    end
  end
end
