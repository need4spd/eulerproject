p = "0123456789".split("").permutation.to_a

sum_of_result = 0

rule = {"1"=>2, "2"=>3, "3"=>5, "4"=>7, "5"=>11, "6"=>13, "7"=>17}
p.each do |pandigital|
  s=pandigital.join("")
  
  isRight = true

  rule.each do |k, v|
    
    #puts "#{k}, #{v}, #{s}, #{s[k.to_i, 3]}"
    
    if not s[k.to_i, 3].to_i % v == 0
      isRight = false
      break
    end
  end
  
  if isRight
    sum_of_result += s.to_i
  end
end

puts sum_of_result
